import socket
import time
import re
'''
This code takes HL7 messages from the 'hl7_messages.txt' file and fires them
one at a time at the associated endpoint listed in the .txt file. What and where
these messages send can be altered by editing the .txt file but the format but be
followed exactly by first listing the endpoint following 'endpoint=' and the
same with the port - 'port=' with the HL7 message following after a new line.
If you wish to send another message, start it after a new line below the last 
HL7 message line.

To Run this file just run the main.exe file and make sure your NHS VPN is turned on.
Author: Oliver Webb - Capacitas 
'''


def read_hl7_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()

        # Split messages by blank lines and endpoint markers
        message_blocks = [block.strip() for block in re.split(r"\n\s*\n(?=endpoint=)", content) if block.strip()]
        messages = []

        for idx, block in enumerate(message_blocks, start=1):
            try:
                lines = block.strip().split("\n")

                if len(lines) < 3:  # Ensure we have endpoint, port, and message
                    print(f"\nWARNING: Skipping Message {idx} due to insufficient lines. Entire block is invalid.\n")
                    continue

                endpoint_match = re.search(r"endpoint=(.+)", lines[0])
                port_match = re.search(r"port=(\d+)", lines[1])

                if not endpoint_match or not port_match:
                    print(
                        f"\nWARNING: Skipping Message {idx} due to missing endpoint or port. Entire block is invalid.\n")
                    continue

                endpoint = endpoint_match.group(1).strip()
                port = int(port_match.group(1).strip())
                hl7_message = "\n".join(lines[2:])

                messages.append((idx, endpoint, port, hl7_message))

            except Exception as e:
                print(f"\nERROR processing Message {idx}: {e}\n")

        return messages
    except Exception as e:
        print(f"\nERROR reading file: {e}")
        return []


def format_hl7_message(input_message):
    segment_headers = ["MSH", "EVN", "PID", "PD1", "PV1"]
    for header in segment_headers:
        input_message = input_message.replace(header, f"\r{header}")
    return input_message.strip()


def send_hl7_message(idx, endpoint, port, hl7_message):
    hl7_mllp_message = b'\x0b' + hl7_message.encode('utf-8') + b'\x1c\r'

    try:
        with socket.create_connection((endpoint, port), timeout=10) as sock:
            sock.sendall(hl7_mllp_message)
            time.sleep(1)
            response = sock.recv(1024)

            if response:
                decoded_response = response.decode('utf-8', errors='ignore')

                if "MSA|AE|" in decoded_response or "MSA|AR|" in decoded_response:
                    print(f"\nERROR: Message {idx} was **rejected** by the server!")
                elif "MSA|AA|" in decoded_response:
                    print(f"\nSUCCESS: Message {idx} was **accepted** by the server!")
            else:
                print(f"\nNo response received for Message {idx}!")
    except socket.timeout:
        print(f"\nERROR: Connection timed out for Message {idx}!")
    except ConnectionRefusedError:
        print(f"\nERROR: Connection refused for Message {idx}! Is the server running?")
    except Exception as e:
        print(f"\nERROR processing Message {idx}: {e}")


def main():
    filename = "hl7_messages.txt"
    messages = read_hl7_from_file(filename)

    if messages:
        for idx, endpoint, port, hl7_message in messages:
            try:
                print(f"\nSending HL7 Message {idx} to {endpoint}:{port}...")
                formatted_message = format_hl7_message(hl7_message)
                send_hl7_message(idx, endpoint, port, formatted_message)
            except Exception as e:
                print(f"\nERROR processing Message {idx}: {e}")
    else:
        print("No valid HL7 messages found.")


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")


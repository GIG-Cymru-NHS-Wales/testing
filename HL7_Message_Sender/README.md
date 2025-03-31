# HL7 Message Processor

## Overview
This Python script reads HL7 messages from `hl7_messages.txt`, processes them, and sends them to a specified destination. Users must modify the template in the script to customize the message content before sending.

## Features
- Reads HL7 messages from a text file (`hl7_messages.txt`)
- Allows modification of message templates
- Sends HL7 messages to a specified endpoint
- Uses `hl7` Python library for message handling

## Prerequisites
Ensure you have the following installed before running the script:

- Python 3.x
- Required dependencies (install via pip):
  ```sh
  pip install hl7 requests
  ```

## Project Structure
```
├── hl7_processor.py  # Main script for processing HL7 messages
├── hl7_messages.txt  # File containing HL7 messages
├── README.md         # Documentation
```

## Usage
### 1. Modify the HL7 Message Template
Open `hl7_messages.txt` and customize the HL7 message format according to your requirements. Ensure the correct segment structure is followed. You can add as many of these messages as you like as long as they are seperated by a 'return key' and all the messages will be sent sequentially. 

Example HL7 message format:
```
endpoint= **Add Endpoint**
port=** Add Port Number**
MSH|^~\&|SendingApp|SendingFac|ReceivingApp|ReceivingFac|20250331||ORM^O01|123456|P|2.3
PID|1||12345^^^Hospital^MR||Doe^John||19800101|M
```

### 2. Run the Script
Execute the script to read and send HL7 messages: Run Hl7SenderV1.0.exe

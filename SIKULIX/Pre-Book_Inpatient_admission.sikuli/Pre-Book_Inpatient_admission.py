Date_Referral_Received = ""
Management_Intent = "1"
HCP = "AMO"
Service = "180000"
Location = "633AA"
Source_of_Referral = "1"
Category_of_Patient = "02"
Priority_on_letter = "3"
HCP_Priority = "3"
Outcome = "41"

Reason = "2"
arrival_time = "2000"
location = "1008"
#Theatre_Plan = "0"

click("1742815611245.png")
wait(2)
click("1742815689505.png")
click("1742815779285.png")
click(Pattern("1742826942014.png").similar(0.86).targetOffset(45,-1))
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Management_Intent)
type(Key.TAB)
type(HCP)
type(Key.TAB)
type(Service)
type(Key.TAB)
type(Location)
type(Key.TAB)
type(Source_of_Referral)
type(Key.TAB)
type(Key.TAB)
type(Category_of_Patient)
type(Key.TAB)
type(Priority_on_letter)
type(Key.TAB)
type(HCP_Priority)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Outcome)

click("1742828410495.png")
click(Pattern("1742828503391.png").targetOffset(-47,0))
type(Key.TAB)
type(Reason)
click(Pattern("1742829012557.png").similar(0.85).targetOffset(123,0))
click("1742829065511.png")
type(Key.TAB)
type(arrival_time)
type(Key.TAB)
type(location)
#type(Key.TAB)
#type(Theatre_Plan)
type(Key.ENTER)
type(Key.ENTER)





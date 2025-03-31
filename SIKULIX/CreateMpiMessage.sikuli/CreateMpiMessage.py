#Tester Login - Enter your login details below
username = ""
password = ""

Case_no = "M8039816"
Admission_Time = "1100"
Arrival_Time = "1055"  
Admitting_Clinician = "DMP"
#Enter Speciality code for 'Admitting Service'
Admitting_Service = "800000"  
#Enter Speciality code for 'Admitting Location'
Admitting_Location = "62101"
#Enter Speciality code for 'Admitting Location'
Admit_Method = "26"


#click(Pattern("usernameInput.png").exact().targetOffset(-33,-3))
#type(username)
#type(Key.TAB)
#type(password)
#type(Key.ENTER)
#doubleClick("1740668337738.png")
#wait(Pattern("1740668472485.png").similar(0.75),10)
#doubleClick(Pattern("1740668472485.png").similar(0.75))
#click(Pattern("1742808698157.png").similar(0.85).targetOffset(-20,-3))
#type(Case_no)
#type(Key.ENTER)
#wait(5)

click("1742809092416.png")
wait(2)
click("1742809156133.png")
click("1742809178665.png")
wait(3)
doubleClick(Pattern("1742809381117.png").similar(0.89).targetOffset(-14,-2))
type(Admission_Time)
type(Key.TAB)
type(Arrival_Time)
click(Pattern("1742809486618.png").similar(0.89).targetOffset(-50,0))
type(Admitting_Clinician)
type(Key.TAB)
type(Admitting_Service)
type(Key.TAB)
type(Admitting_Location)
type(Key.TAB)
type(Admit_Method)
type(Key.ENTER)






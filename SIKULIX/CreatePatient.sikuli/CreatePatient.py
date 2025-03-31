#Tester Login - Enter your login details below
username = ""
password = ""

#Patient Details:
NHS_Number = "3464710289"
surname = "Moran"
forname = "Noam"
title = "Prof."
sex = "M"
dob = "27061991"
address = "1356 BRIGANTINE PLACE CARDIFF"
postcode = "CF104LN"
short_postcode = "CF10"

holder = "AZO"

click(Pattern("usernameInput.png").exact().targetOffset(-33,-3))
# Type into the selected text box
type(username)

# Optionally, press TAB or ENTER
type(Key.TAB)
type(password)
type(Key.ENTER)

#doubleClick("1740668337738.png")
wait(5)
#click("1740744220993.png")
wait(Pattern("1740668472485.png").similar(0.75),10)
doubleClick(Pattern("1740668472485.png").similar(0.75))
doubleClick(Pattern("1740668546646.png").similar(0.96))
wait(2)
doubleClick(Pattern("1740668647849.png").similar(0.89))
wait(6)
wait(Pattern("1740742510099.png").similar(0.04),10)
#Fill in details:
click(Pattern("1740671246370.png").similar(0.78).targetOffset(123,-1))
paste(NHS_Number)
click(Pattern("1740670012915.png").similar(0.89))
click(Pattern("1740672169651.png").similar(0.91).targetOffset(-7,-1))
type(title)
type(Key.TAB)
type(sex)
type(Key.TAB)
type(surname)
type(Key.TAB)
type(forname)
type(Key.TAB)
type(Key.BACKSPACE)
type(Key.BACKSPACE)
type(Key.BACKSPACE)
type(Key.BACKSPACE)
type(dob)
type(Key.TAB)
type(Key.TAB)
type(postcode)
type(Key.TAB)
wait(10)
wait(Pattern("1740742649210.png").similar(0.15),10)
click(Pattern("1740670579001.png").similar(0.87))
click(Pattern("1740672227051.png").similar(0.92).targetOffset(3,1))
wait("1740742381279.png",10)
click(Pattern("1740671585571.png").similar(0.85).targetOffset(-93,0))
type(short_postcode)
type(Key.ENTER)
wait(3)
wait(Pattern("1740742435346.png").similar(0.04),10)
type(Key.ENTER)
wait(1)
click(Pattern("1742988074418.png").similar(0.82).targetOffset(0,-9))
wait(3)
type(Key.TAB)
type(Key.TAB)
type(holder)
type(Key.ENTER)
type(Key.TAB)
type(Key.ENTER)
#click("1742988226316.png")

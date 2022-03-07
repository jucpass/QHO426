print ("Program Started!\nPlease enter a standard character:")
char=input()
value=0

if len(char)==1:
  value=ord(char)
  print(f"The ASCII code for {char} is {value}.\nProgram ended!")
else:
  print ("Invalid character or out of lengh")
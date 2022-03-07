print ("Program Started!\nPlease enter an ASCII code:")
code=int(input())
value=0

if code in range(32,127,1):
  value=chr(code)
  print(f"The character represented by the ASCII code {code} is {value}.\nProgram ended!")
else:
  print ("Invalid character or out of lengh")
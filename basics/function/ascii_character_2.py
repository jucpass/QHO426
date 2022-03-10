print ("Program started!")
x = abs(int(input ("Please enter ASCII code: ")))
#if x >= 32 and x <=126:
if x in range(32,127,1):
  print (f"The ASCII is {x} and Character is {chr(x)}")
else:
  print ("not valid code or out of range.")

print ("Program ended!")
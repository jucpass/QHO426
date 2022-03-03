h = input("Are you happy?")
k = input ("Do you know it?")

if h.lower() == "yes" and k.lower() == "yes":
  print ("Clap your hands!")
elif h.lower() == "yes" and k.lower() == "no":
  print ("show your happiness")
else:
  print ("help is available. Talk to me!")
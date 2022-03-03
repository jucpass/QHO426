name = input("Enter your name:")

#len() function to count lenght of tring
if len(name) > 9:
  print ("Your name is way too long to remember. Can I use a nickname please?")
  print ("Nice to meet you anyway, {}!".format(name))

elif len(name)<=3:
  print ("This is very short, easy to remember!")
  print ("Nice to meet you anyway, {}!".format(name))
else:
  print ("Your name is very short")
  print ("Nice to meet you anyway, {}!".format(name))

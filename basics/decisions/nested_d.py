print("Were should I look?")
answer = input()

if answer.lower() == "in the bedroom":
  print ("Where in the bedroom should I look?")
  answer2 = input()
  if answer2.lower() == "under the bed":
    print ("Found some shoes, but no battery!")
  else:
    print ("Found some mess, but no battery")
elif answer.lower() == "in the bathroom":
  print ("Where in the bathroom should I look?")
  answer2 = input() 
  if answer2.lower() == "in the bathtub":
    print ("Found rubber duck, but no battery!")
  else:
   print ("Found wet surface, but no battery")
elif answer.lower() == "in the lab":
  print ("Where in the lab should I look?")
  answer2 = input() 
  if answer2.lower() == "on the table":
    print ("Yes! I found my battery!")
  else:
   print ("Found some tools but no battery.") 
else:
  print ("I do not know where that is but I will keep looking.")
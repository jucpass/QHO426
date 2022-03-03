age = int(input("Enter age:"))
ch = int(input("Enter number of children:"))

if age > 25 and ch > 0:
  print ("You are a young parent")
  print (f"Next year you gonna be {age +1} years old")
elif age > 55 and ch > 0:
  print ("Your child will support you in old age")
elif age < 18 or ch == 0:
  print ("There is enough time to have a child if you want")
else:
  print ("You are not soo young :(")
  print ("we are going to live a long life anyway!")
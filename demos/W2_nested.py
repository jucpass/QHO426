salary = float(input("Enter Salary: "))
years = int(input("Year in the position: "))

if years > 2:
  if salary < 25000:
    salary = salary*1.1
    print (f"Your new salary will be {salary}")
  else:
   salary = salary + 100
   print (f"Small change, you will earn now {salary}")
elif years >=1:
  print ("No salary increase, sorry")
else:
  if salary < 15000:
    print ("Ooops! You salary should be 20000.")
    salary = 20000
print ("let us work for the good of the company")

  

  
print ("Whats your name?")
name = input()
print ("Whats your Age in years?")
age = int(input())
print ("How tall are you in meters?")
height = float(input())
print ("How much do you weight in kilos?")
weight = float(input())

bmi = weight/(height*height)

print (f"{name} you {age} and your BMI is {bmi:.2f}:")

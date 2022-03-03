print ("Enter first number: ")
n1 = int(input())

print ("Enter Second number: ")
n2 = int(input())

print ("Enter Third number: ")
n3 = int(input())

odd = 0
even = 0

if n1%2 == 0:
  even = even + 1
else:
  odd = odd + 1

if n2%2 == 0:
  even = even + 1
else:
  odd = odd + 1

if n3%2 == 0:
  even = even + 1
else:
  odd = odd + 1
print (f"number of even: {even} Number of odds: {odd}")

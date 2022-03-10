import random
def play_guess_the_number():
  min = int(input("Enter the minimum value: "))
  max = int(input("Enter the maximum value: "))
  
  x = random.randrange(min, max)
  
  print (f"I'm thinking of a number between {min} and {max}. Can you guess what it is?")
  
  while True:
    guess = int(input("Have a guess: "))
    if guess < x:
      print ("Your guess is too low!\n")
    elif guess > x:
      print ("Your guess is too high!\n")
    else:
      break
    print ("Try again!")
  
  print ("Congrats, you guessed the number!")

play_guess_the_number()
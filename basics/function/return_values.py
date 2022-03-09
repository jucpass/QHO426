def sum_weights(beep,boop):
  total = beep+boop
  return total

def calc_avg_weight(beep,boop):
  avg = sum_weights(beep,boop)/2
  return avg
  
def run():
  print("What is the weight of Beep?")
  beep = int(input())
  print("What is the weight of Boop?")
  boop = int(input())

  print ("What would you like to calculate (sum or average)?")
  choice = input()
  if choice.lower() == 'average':
    print (f"The average weight of Beep and Bop's weight is {calc_avg_weight(beep,boop)}.")
    calc_avg_weight(beep,boop)
  elif choice.lower() == 'sum':
    print (f"The sum of Beep and Bop's weight is {sum_weights(beep,boop)}.")
  else:
    print ("Invalid Option")

run()
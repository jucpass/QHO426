def display_ladder (steps):
  print ("|   |\n ***\n" * steps)

def create_ladder():
  print("Enter the number of steps")
  steps = int(input())
  display_ladder(steps)

  
create_ladder()
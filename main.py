def ascii_art_box(word):
  message = "* Hello {} *".format(word)
  print ("*" * len(message))
  print (message)
  print ("*" * len(message))
def lower_case(word):
 word = word.lower()
 print (word)
def upper_case(word):
 word = word.upper()
 print (word)
def mirrored(word):
 for i in range(len(word),0,-1):
   print (f"{word[i]}")
def repeat(word,rep):
  for i in range (rep):
   print (word)
def run():
  print("Insert a word to manipulate:")
  word = input()
  print("1) Display in a Box – display the word in an ascii art box\n2) Display Lower-case – display the word in lower-case e.g. hello\n3) Display Upper-case – display the word in upper-case e.g. HELLO\n4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH\n5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
  choice = int(input())

  if choice == 1:
   ascii_art_box(word)
  elif choice == 2:
   lower_case(word)
  elif choice == 3:
   upper_case(word)
  elif choice == 4:
   mirrored(word)
  elif choice == 5:
   print ("How many times to repeat?")
   rep = input()
   repeat(word,repeat)
  else:
   print ("Invalid Option")

run()
    

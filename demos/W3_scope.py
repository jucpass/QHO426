def inc_a(a):

  a = a+1
  return a

def dec_a(a):
  a=a-1
  return a

def run():
  a=7
  a = dec_a(inc_a(a+2))
  inc_a(a)
  inc_a(a)
  print (f"the value of A is:{a}")

run()
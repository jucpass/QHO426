def cross_bridge(step):
  for i in range(step):
    print ("Crossed step")
  if step>5:
    print ("The bridge is collapsing!") 
  else:
    print ("we must keep going!")

cross_bridge(6)
cross_bridge(3)
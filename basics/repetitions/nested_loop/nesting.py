print ("Please enter a sequence")
k = input() #read the sequence
print ("Please enter the character for the marker")
y = input() #read the marker

first=0 #variable to use store the first marker
second=0 #variable to use store the first marker


for i in range(len(k)):
 print ("=",k[i],end="") # print used to visualize 
 if k[i]==y: # find the first marker
   first=i #load the position of first marker
   break #finish first loop
for t in range(first+1, len(k), 1): #start from the next position of first marker
   print ("=",k[t],end="")# print used to visualize 
   if k[t]==y: #find the second marker
    second=t-1 #load the position to variable second, less one position as the marker doesnt count

print (f"result:{second-first}") #calculate the higher distance less the lower, the diference is the distance
   

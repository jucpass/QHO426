print ("Please enter a sequence")
k = input() #store the sequence
print ("Please enter the character for the marker")
y = input()

first=0
second=0
t=0


for i in range(len(k)):
 print (k[i],end="") # print used to visualize 
 if k[i]==y: # find the first marker
   first=i #load the position of first marker
   break #finish first loop
for t in range(first+1, len(k), 1): #start from the next position of first marker
   print (k[t],end="")# print used to visualize 
   if k[t]==y: #find the second marker
    second=t-1 #load the position to variable second, less one position as the marker doesnt count

print (f"\nThe distance between the markers is:{second-first}") #calculate the higher distance less the lower, the diference is the distance
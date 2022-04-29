N = int(input()) 
M = int(input()) 

for i in range(2, m) :
   if i%m == 0:
      print(i, end=" ")
   if i%2 == 0:
      print("Even") 
   else:
      print("Odd") 

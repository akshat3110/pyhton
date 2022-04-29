n = int(input())
m = int(input())
l = []
for i in range(1,n):
  if(i%m == 0):
    if(i%2 == 0):
      print(i,"EVEN")
    else:
      print(i,"ODD")

Write a program to print every integer b/w 1 to n divisible by m also check wheather the divisible is even or odd

n=int(input("enter n : "))
m=int(input("enter m : "))

for i in range(1,n+1):
  if(i%m==0):
    if(i%2==0):
      print("{0} is divisible by {1} and is even no.".format(i,m))
    else:
      print("{0} is divisible by {1} and is odd no.".format(i,m))
enter n : 10
enter m : 5
5 is divisible by 5 and is odd no.
10 is divisible by 5 and is even no.



Wap to find largest no. of list entered through keyboard

l=[int(x) for x in input().split()]
print(max(l))
111 82
111




WAP to to take a no. n and returns a randomly generated exacly n digit no.

import random
n=int(input())
sv=0
lv=9
for i in range(n):
  if i==0:
    sv=0
    lv=9
  else:
    lv=(lv*10)+9
    if(i==1):
      sv=10
    else:
      sv=sv*10

print(random.randint(sv, lv))
4
8933

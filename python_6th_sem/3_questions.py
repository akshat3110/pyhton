add two numbers

t=int(input())
while(t>0):
  a,b=input().split()
  a,b=int(a),int(b)
  print(a+b)
  t-=1
2
2 3
5
3 6
9




find reminder

t=int(input())
while(t>0):
  a,b=input().split()
  a,b=int(a),int(b)
  print(a%b)
  t-=1
2
40 15
10
100 200
100



sum of 1 and last digit

t=int(input())
while(t>0):
  a=input()
  f=int(a[0])
  l=int(a[-1])
  print(f+l)
  t-=1
2
25364
6
536475
10

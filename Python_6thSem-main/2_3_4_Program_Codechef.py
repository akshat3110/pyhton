#add two numbers
x = int(input())
y = int(input())
print(x+y)
t+=1


#find remainder
print(x%y)

#find sum of first ans last digit
last = x%10
first = 0
while(x >= 10):
  x = x//10
first = x ;
print(first+last)

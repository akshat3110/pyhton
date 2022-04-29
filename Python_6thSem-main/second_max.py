t= int(input())
while t:
    x,y,z = [int(a) for a in input().split() ]
    
    ma = max(x,y,z)
    mi = min(x,y,z)
    
    if (x != ma) and (x != mi):
        print(x)
    elif (y != ma) and (y != mi):
        print(y)
    else: print(z)
    t-=1

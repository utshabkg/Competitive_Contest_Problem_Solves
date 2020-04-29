i=lambda:map(int,input().split())
a,b = i()

y = 1

while True:
    if(3*a > 2*b):
        print(y)
        break
    else:
        y = y+1
        a = 3*a
        b = 2*b
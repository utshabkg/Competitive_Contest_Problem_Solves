i=lambda:map(int,input().split())
a, b = i()


while True:
    if a==0 or b==0:
        break
    elif a>=2*b and a!=0 and b!=0:
        a = a % (2*b)
    elif b>=2*a and a!=0 and b!=0:
        b = b % (2*a)
    else:
        break

print(a, b)
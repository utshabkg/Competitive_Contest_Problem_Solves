inp=lambda:map(int,input().split())
for _ in range(int(input())):
    a1,b1=inp()
    a2,b2=inp()
    s1=a1+a2;s2=a1+b2
    s3=b1+a2;s4=b1+b2
    if (a1+a2==b1 or a1+b2==b1 or b1+b2==a1 or b1+a2==a1):
        print("YES")
    else:
        print("NO")
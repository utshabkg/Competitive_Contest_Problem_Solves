inp=lambda:map(int,input().split())
t = int(input())

for i in range(t):
    n,m = inp()

    if n==1:
        print(0)
        continue
    elif n==2:
        print(m)
        continue
    else:
        print(2*m)
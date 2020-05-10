inp=lambda:map(int,input().split())
t = int(input())

for j in range(t):
    n, k = inp()
    x = n*(k//(n-1))

    if k%(n-1)==0:
        x-=1
    else:
        x+= k%(n-1)
    print(x)


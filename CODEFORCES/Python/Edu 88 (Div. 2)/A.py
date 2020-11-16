import math

inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    c, j, p = inp()

    each = int(c/p)

    high, maxm = 0, 0

    if each>=j:
        print(j)
    else:
        high = each
        j -= high
        if high==j:
            print(0)
        else:
            

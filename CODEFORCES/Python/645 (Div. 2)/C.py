import math
inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = inp()

    if x1==x2 or y1==y2:
        print(1)
    
    else:
        print(abs(x2-x1) * abs(y2-y1)+1)
    
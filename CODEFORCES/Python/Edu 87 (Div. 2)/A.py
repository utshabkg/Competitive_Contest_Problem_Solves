import math
inp=lambda:map(int,input().split())
t = int(input())

for _ in range(t):
    a,b,c,d = inp()
    
    # l = list(inp())

    if b>=a:
        print(b)
        continue
    if d>=c:
        print(-1)
        continue
    else:
        print(b + math.ceil((a-b)/(c-d)) * c)
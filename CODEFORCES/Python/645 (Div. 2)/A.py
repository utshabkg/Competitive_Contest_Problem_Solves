import math
inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    n,m = inp()
    
    # l = list(inp())

    print(math.ceil((n*m)/2))
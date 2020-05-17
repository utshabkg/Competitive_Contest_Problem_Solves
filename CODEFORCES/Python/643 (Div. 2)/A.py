import math

inp=lambda:map(int,input().split())
t = int(input())

for _ in range(t):
    # n = int(input())
    n,k = inp()
    # l = list(inp())
    l = []
    l.append(n)
    sum = 0
    for i in range(k):
        a = list(map(int, str(sum))) 
        # print(a)
        sum = l[i] + max(a) * min(a)
        l.append(sum)

    print(sum)
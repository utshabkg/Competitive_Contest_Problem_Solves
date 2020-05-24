inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    # n,k = inp()
    l = list(inp())
    d = []
    l = sorted(l)
    for i in range(1, len(l)):
        d.append(abs(l[i-1] - l[i]))

    print(min(d))
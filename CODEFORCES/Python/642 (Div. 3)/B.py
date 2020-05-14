inp=lambda:map(int,input().split())
t = int(input())

for _ in range(t):
    n,k = inp()
    a = list(inp())
    b = list(inp())

    sa = sorted(a)
    sb = sorted(b)
    sb = sb[::-1]

    for i in range(k):
        if sa[i]<sb[i]:
            sa[i],sb[i] = sb[i], sa[i]
        else:
            pass
    
    print(sum(sa))
    
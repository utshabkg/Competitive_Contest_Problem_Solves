inp=lambda:map(int,input().split())
n, m = inp()
a = list(inp())

sr = sorted(a)
total = 0

for i in range(m):
    if sr[i]<0:
        total += sr[i]
    
print(-total)


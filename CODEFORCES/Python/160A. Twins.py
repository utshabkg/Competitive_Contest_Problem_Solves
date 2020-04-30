inp=lambda:map(int,input().split())
n = int(input())
l=list(inp())
l.sort()
s = sum(l)
# print(l,s)
# print(l[-n])

c = 0
maxm=0

for i in range(1, n+1):
    if s < maxm:
        break
    else:
        s = s - l[-i]
        maxm = maxm + l[-i]
        c = c+1

print(c)

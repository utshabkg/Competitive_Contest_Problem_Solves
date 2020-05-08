inp=lambda:map(int,input().split())
n = int(input())
a = list(inp())
m = int(input())
b = list(inp())

maxm = 0
l=[]

for i in range(m):
    for j in range(n):
        if b[i]/a[j] - b[i]//a[j] == 0:
            maxm = max(maxm, int(b[i]/a[j]))
            l.append(int(b[i]/a[j]))

print(l.count(maxm))
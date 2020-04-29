i=lambda:map(int,input().split())

n = int(input())
maxm, capa = 0, 0
for j in range(n):
    a,b = i()
    if(j==0):
        capa = b
    if(j>0):
        maxm = max(capa, maxm)
        capa = capa + b - a
    # print(capa, maxm)

print(maxm)



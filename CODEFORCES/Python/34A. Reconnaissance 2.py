import math

n = int(input())
inp=lambda:map(int,input().split())
l=list(inp())
minm = 1000
a, b = 0, 0


# for i in range(n):
for j in range(n):
    # if i==j:
    #     continue
        # else:
    if j == n-1:
        if abs(l[j]-l[0]) < minm:
            a,b = j, 0
            minm = abs(l[0]-l[j])
    elif abs(l[j]-l[j+1]) < minm:
        a,b = j, j+1
        minm = abs(l[j]-l[j+1])
            
    
print(a+1, b+1)

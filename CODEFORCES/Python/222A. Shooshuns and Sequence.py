inp=lambda:map(int,input().split())
n,k = inp()
l = list(inp())

temp = l[k-1]
count = 0

while n and l[n-1] == l[-1]:
    	n -= 1
print([-1, n][k > n])
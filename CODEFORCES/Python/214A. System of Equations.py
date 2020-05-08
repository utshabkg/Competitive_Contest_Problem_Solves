inp=lambda:map(int,input().split())
n, m = inp()

count=0
l=[]
for i in range(max(n,m)+1):
    for j in range(max(n,m)+1):
        if i**2+j==n and i+j**2==m:
            if l.count(str(i)+str(j))<1 or l.count(str(j)+str(i))<1:
                count += 1
                l.append(str(i)+str(j))
                # print(l)

print(count)
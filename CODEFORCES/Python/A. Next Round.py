#n, k = map(int, input().split())
i=lambda:map(int,input().split())
n,k=i()
l=list(i())
count = 0

for j in range(n):
    if l[j]!=0 and l[j]>=l[k-1]:
        count += 1

print(count)

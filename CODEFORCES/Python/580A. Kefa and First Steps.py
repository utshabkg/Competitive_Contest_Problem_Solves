i=lambda:map(int,input().split())
n = int(input())
l=list(i())
 
maxm = 1
c = 1
# l.append(0)
 
# print(len(l))
for j in range(n):
    if n == 1:
        break
 
    if j==n-1:
        if c>maxm:
            maxm = c
        break
 
    if l[j]>l[j+1]:
        maxm = max(c, maxm)
        c = 1
    if l[j]<=l[j+1]:
        c += 1

        
    # print("loop",j,":",l[j], l[j+1])
    # print(c, maxm)
    # print()
print(maxm)
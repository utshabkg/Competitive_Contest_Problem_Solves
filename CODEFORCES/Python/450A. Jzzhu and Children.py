#not solved yet

i=lambda:map(int,input().split())
n,k=i()
l=list(i())

pos = {}

for li in range(n):
    pos[li] = l[li]
    # print(pos)

j = 0
c = 0
# print(pos[0]<=2)
for j in pos:
    if pos[j]<=2:
        del pos[j]
        c = j
    else:
        pos[j] = pos[j] - 2
        # c = j
    
    print(j)
    print(pos)

    j += 1
    if j==n-1:
        j = c+1
    if j==n:
        break
    
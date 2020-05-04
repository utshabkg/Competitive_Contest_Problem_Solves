#not solved yet

i=lambda:map(int,input().split())
n,k=i()
l=list(i())

pos = {}

for li in range(n):
    pos[li] = l[li]
    # print(pos)

j = 0
c = []
d = []
for z in range(n):
    c.append(z)
# print(pos[0]<=2)
while True:
    if bool(pos)==False:
        break
    for j in c:
        if bool(pos)==False:
            break
        if pos[j]<=k:
            del pos[j]
            d.append(j) 
        else:
            pos[j] = pos[j] - k

        if j==c[-1]:
            break
        # print(j)
        # print(pos.values()) 
        # print(c,d)
    c = [item for item in c if item not in d]

print(d[-1]+1)
    
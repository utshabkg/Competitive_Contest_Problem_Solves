i=lambda:map(int,input().split())

n = int(input())
l = list(i())
m = int(input())
q = list(i())

p, v, j = 0, 0, 0
pos = {}

for li in l:
    pos[li] = j
    j += 1
# print(pos)
for qi in q:
    v += pos[qi] + 1
    p += n - pos[qi]

###  TLE  ###
# for x in range(m): #and x in range(m):
#     for y in range(0,n,1):
#         if q[x]==l[y]:
#             v += 1
#             break
#         else:
#             v += 1
#     p = v - n + 1
        
    # for z in range(n-1,-1, -1):
    #     if q[x]==l[z]:
    #         p += 1
    #         break
    #     else:
    #         p += 1
# p = v - n + 1
print(v, p)
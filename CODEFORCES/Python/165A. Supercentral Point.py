n=int(input())
x=[list(map(int,input().split()))for i in range(n)]

count = 0

for i in range(n):
    u, d, l, r = 0, 0, 0, 0
    for j in range(n):
        if i==j:
            continue
        else:
            if x[i][0]>x[j][0] and x[i][1]==x[j][1]:
                r = 1
            # else:
            #     r = 0
            if x[i][0]<x[j][0] and x[i][1]==x[j][1]:
                l = 1
            # else:
            #     l = 0
            if x[i][0]==x[j][0] and x[i][1]<x[j][1]:
                d = 1
            # else:
            #     d = 0
            if x[i][0]==x[j][0] and x[i][1]>x[j][1]:
                u = 1
            # else:
            #     u = 0
    if u+d+l+r == 4:
        count += 1

print(count)
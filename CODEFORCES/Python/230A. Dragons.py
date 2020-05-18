#NOT solved yet
inp=lambda:map(int,input().split())
s, n = inp()
x=[list(map(int,input().split()))for i in range(n)]

a = []
b = []
for i in range(n):
    a.append(x[i][0])
    b.append(x[i][1])
# sr = sorted(l)

for i in range(n):
    # if i==0:
    dragon, bonus = min(a), b[a.index(min(a))]

    # print(dragon, bonus, a.index(min(a)))

    if s<=dragon:
        print("NO")
        exit()
    else:
        s+=bonus
        if len(a)>1:
            # print(b[a.index(min(a))])
            del a[a.index(min(a))]
            del b[a.index(min(a))+1]
            print(a,b)

print("YES")
    
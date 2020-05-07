l = [2, 7]
for i in range(2, 100000,):
    l.append(l[i-1] + l[i-1]-l[i-2]+3)


for _ in range(int(input())):
    n = int(input())
    out, index, count = 0, 0, 0
    outl = []

    for j in range(len(l)):
        outl.append(l[j])
        if l[j]>=n:
            # out = l[j]
            # index = j-1
            break
    for k in range(len(outl)-1, -1, -1):
        if n<2:
            break
        if outl[k]<=n:
            n = n - outl[k]
            count += 1
    # print(out, index, outl)
    print(count)

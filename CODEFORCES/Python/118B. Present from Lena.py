n = int(input())

for i in range(n+1):
    l = []
    for j in range(i+1):
        l.append(j)
    for j in range(1, i+1):
        l.append(l[-j]-j)
    q = list([" "]*(n-i))
    print(*q,*l)

for i in range(n-1,-1,-1):
    l = []
    for j in range(i+1):
        l.append(j)
    for j in range(1, i+1):
        l.append(l[-j]-j)
    q = list([" "]*(n-i))
    print(*q,*l)
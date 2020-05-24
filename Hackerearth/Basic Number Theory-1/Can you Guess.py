n = int(input())
for i in range(n):
    q = int(input())
    s = 0
    for j in range(1, q):
        if (q%j==0):
            s += j
    print (s)
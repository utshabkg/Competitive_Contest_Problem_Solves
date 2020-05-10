inp=lambda:map(int,input().split())
t = int(input())


for i in range(t):
    n = int(input())
    count = 0
    q, r = n, 0
    l = []
    if n<10:
        print(1)
        print(n)
        continue
    s = str(n)
    x = len(s)-1
    for j in range(0, len(s)):
        if s[j]!='0':
            l.append(int(s[j]) * pow(10, x))
            x-=1
        else:
            x-=1
            continue
    
    print(len(l))
    print(*l)
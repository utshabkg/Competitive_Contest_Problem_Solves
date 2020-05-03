T = int(input())

i=lambda:map(int,input().split())

while T >0:
    n,k=i()
    l = list(i())
    s=list(set(l))
    if(len(s)>k):
        print(-1)
    else:
        s.extend([l[0]]*(k-len(s)))
        # print(s)
        s=s*n
        # print(s)
        print(n*k)
        print(*s)
    T -= 1
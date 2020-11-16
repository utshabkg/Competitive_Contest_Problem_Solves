#Not solved yet

# inp=lambda:map(int,input().split())
# n,k = inp()
for _ in range(int(input())):
    n = int(input())
    l = 1; r = n
    i = 1; a = [0]*n
    # print(a)
    while i<=n:
        if (r-l+1)%2!=0:
            a[(l+r)//2-1] = i

        else:
            a[(l+r-1)//2-1] = i
        
        if (l+r)//2 <= n/2:
                l = (l+r)//2+i
                r = n
        else:
            l = 1
            r = (l+r)//2-i
        i+=1
        print(a)
    
    # print(a)
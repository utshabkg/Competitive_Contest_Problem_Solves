## WA on test case 2

inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    # n,k = inp()
    l = list(inp())

    even = []; odd = []; d = []; i= 0

    l = sorted(l)
    # while i<len(l)-1:
    #     # d.append(abs(l[i] - l[i+1]))
    #     if abs(l[i] - l[i+1])==1:
    #         del l[i]; del l[i]
    #     else:
    #         i+=1

    # for i in l:
    #     if i%2==0:
    #         even.append(i)
    #     else:
    #         odd.append(i)

    while i<len(l)-1:
        # d.append(abs(l[i] - l[i+1]))
        if abs(l[i] - l[i+1])!=1 and (l[i]%2==0 and l[i+1]%2==0):# or (l[i]%2!=0 and l[i+1]%2!=0)):
            even.append(i);even.append(i+1)
            del l[i]; del l[i]
        elif abs(l[i] - l[i+1])!=1 and (l[i]%2!=0 and l[i+1]%2!=0):
            odd.append(i);odd.append(i+1)
            del l[i]; del l[i]
        else:
            i+=2
    
    i = 0

    while i<len(l)-1:
        if abs(l[i] - l[i+1])==1:# and (l[i]%2==0 and l[i+1]%2==0):# or (l[i]%2!=0 and l[i+1]%2!=0)):
            del l[i]; del l[i]
        else:
            i+=2

    if len(even)%2==0 and len(odd)%2==0 and len(l)==0:
        print("YES")
    else:
        print("NO")
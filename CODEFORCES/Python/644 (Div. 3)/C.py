## WA on test case 2

inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    # n,k = inp()
    l = list(inp())

    even = []; odd = []; d = []; i= 0

    while i<len(l):
        if l[i]%2==0:
            even.append(l[i])
        else:
            odd.append(l[i])
        i+=1
        
    if len(even)%2==0 and len(odd)%2==0:# and len(l)==0:
        print("YES")
        continue
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

    i = 0
    while i<len(l)-1:
        # d.append(abs(l[i] - l[i+1]))
        if abs(l[i] - l[i+1])!=1 and (l[i]%2==0 and l[i+1]%2==0):
            if abs(l[i] - l[i+1])>1:
                even.append(l[i]);even.append(l[i+1])
                del l[i]; del l[i]
            elif abs(l[i] - l[i+1])==0:
                i+=1
                continue
        elif abs(l[i] - l[i+1])!=1 and (l[i]%2!=0 and l[i+1]%2!=0):
            if abs(l[i] - l[i+1])>1:
                odd.append(l[i]);odd.append(l[i+1])
                del l[i]; del l[i]
            elif abs(l[i] - l[i+1])==0:
                i+=1
                continue
        else:
            i+=2
    print(even, odd, l)
    
    i = 0

    while i<len(l)-1:
        if abs(l[i] - l[i+1])==1:# and (l[i]%2==0 and l[i+1]%2==0):# or (l[i]%2!=0 and l[i+1]%2!=0)):
            del l[i]; del l[i]
        elif abs(l[i] - l[i+1])==0:
            i+=1
            continue
        else:
            i+=2

    i = 0
    while i<len(l):
        if l[i]%2==0:
            even.append(l[i])
            del l[i]
        elif l[i]%2!=0:
            odd.append(l[i])
            del l[i]
        else:
            i+=1
        print(even, odd, l)

    if len(even)%2==0 and len(odd)%2==0 and len(l)==0:
        print("YES")
    else:
        print("NO")

    print(even, odd, l)
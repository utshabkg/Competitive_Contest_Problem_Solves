import math
inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    
    l = list(inp())
    l = sorted(l)
    l.insert(0,0)
    pre = 1;count = pre;res = 0
    # i=0

    for i in range(n, 0, -1):
        if l[i]<=i:
            pre += i
            break

    print(pre)

    # while i<len(l):
    #     if len(l)==0:
    #         break

    #     if pre+res>=l[i]:
    #         if res==0:
    #             pre += l.count(l[i])
    #             l = l[l.count(l[i]):]

    #         else:
    #             pre += res + 1
    #             l = l[i+1:]
    #             res = 0
    #             i=0
    #         count = pre
        
    #     else:
    #         res += 1
    #         i+=1
    #     # print(l)
        
    
    # print(count)

# l = [0, 1, 2, 3, 4, 5]
# print(l[-3:])
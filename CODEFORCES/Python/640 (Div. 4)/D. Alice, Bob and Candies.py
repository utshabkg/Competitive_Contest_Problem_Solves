inp=lambda:map(int,input().split())
t = int(input())

for _ in range(t):
    n = int(input())
    l = list(inp())

    r, a, b = 0, 0, 0
    ta,tb=0,0
    i=0;j=-1

    while True:
        if len(l)==0:
            break
        # print(r,ta,tb)
        # print(*l)

        if i==0:
            ta = l[i]
            a += l[i]
            del l[i]
            r += 1
            i += 1
            continue
        if tb<=ta and r%2!=0:
            tb += l[j]
            b += l[j]
            del l[j]
            if tb>ta:
                r += 1
                ta = 0
            if tb<=ta and len(l)==0:
                r += 1
                break
            continue
            

        if tb>=ta and r%2==0:
            ta += l[i-1]
            a += l[i-1]
            del l[i-1]
            if tb<ta:
                r += 1
                tb = 0
            if tb>=ta and len(l)==0:
                r += 1
                break
            continue
    
    print(r, a, b)

            

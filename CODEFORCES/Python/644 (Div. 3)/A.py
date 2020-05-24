inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    # n = int(input())
    a, b = inp()
    ma = max(a, b)
    mi = min(a, b)
    # l = list(inp())

    # if a%2==0 and b%2==0:
    #     if a!=b:
    #         print(pow(m, 2))
    #     else:
    #         print(4*a*b)
    #     continue
    # if a%2!=0 and b%2!=0:
    #     print(pow((m), 2))
    #     continue

    # if a%2!=0 and a>=b:
    #     print((a+1) * (a+1))
    #     continue
    # if b%2!=0 and b>=a:
    #     print((b+1) * (b+1))
    #     continue

    if a!=b:
        if ma>=2*mi:
            print(ma*ma)
        else:
            print(4*mi*mi)
        continue
    else:
        print(4*a*b)
        continue
    
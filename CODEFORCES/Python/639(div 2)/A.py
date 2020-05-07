inp=lambda:map(int,input().split())

for _ in range(int(input())):
    a, b=inp()
    if a == 1 or b == 1 or a + b == 4:
        print("YES")
    else:
        print("NO")
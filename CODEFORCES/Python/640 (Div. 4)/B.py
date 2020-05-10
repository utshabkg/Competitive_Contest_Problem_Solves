inp=lambda:map(int,input().split())
t = int(input())


for _ in range(t):
    n,k = inp()
    if n % 2 == 0 and n >= 2 * k:
        print("YES")
        print(*([2] * (k - 1)), n - 2 * k + 2)
    elif n >= k and (n - k + 1) % 2 == 1:
        print("YES")
        print(*([1] * (k - 1)), n - k + 1)
    else:
        print("NO")


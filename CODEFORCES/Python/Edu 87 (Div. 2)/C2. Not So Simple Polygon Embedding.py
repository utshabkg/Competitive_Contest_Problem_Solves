inp=lambda:map(int,input().split())
t = int(input())

import math

for i in range(t):
    n = int(input())
    # print(math.pi)
    # print(a)
    ans = 1/math.tan(math.pi / (2*n - 1))
    print(ans)

    # print(math.tan(45))

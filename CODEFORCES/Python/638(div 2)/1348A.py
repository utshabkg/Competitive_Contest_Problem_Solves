import math

T = int(input())


while T>0:
    n = int(input())
    a, b = pow(2, n), pow(2, n-1)
    for i in range(1, n//2):
        a = a + pow(2, i)
        b = b + pow(2, i+n//2-1)

    print(int(math.fabs(a-b)))
    T -= 1

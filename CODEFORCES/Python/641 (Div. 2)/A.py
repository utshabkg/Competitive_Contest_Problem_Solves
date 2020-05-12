t = int(input())
inp=lambda:map(int,input().split())

import math

def f_n(n):
    i = 2
    flag = 0
    for i in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            flag = 1
            break
    if flag==1:
        x = i
    else:
        x = n
    return x



for _ in range(t):
    n,k = inp()

    if n%2==0:
        n += 2 * k
    else:
        n += f_n(n) + (k-1)*2
    
    print(n)
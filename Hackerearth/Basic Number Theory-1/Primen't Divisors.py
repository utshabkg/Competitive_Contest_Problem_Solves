##partially solved

import math

t = int(input())

for _ in range(t):
    count = 1; pcount = 0; prod = 1

    n = int(input())

    while n%2==0:
        pcount = 1
        count += 1
        n = n//2

    prod *= count

    for i in range(3, int(math.sqrt(n)+1), 2):
        count = 1
        if n%i==0:
            pcount += 1
            while n%i == 0:
                count += 1
                n = n//i
        prod *= count
    
    if n>2:
        pcount += 1
        prod *= 2
    print(prod - pcount)
    

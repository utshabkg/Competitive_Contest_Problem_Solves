import math
inp=lambda:map(int,input().split())
t = int(input())

def factor(n, k):
    i = 1; s= []
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
            if n // i == i:
                if i<=k:
                    s.append(i) 
            else :
                if i <=k:
                    s.append(i)
                if n//i <=k:
                    s.append(n//i)
        i = i + 1
    sr = sorted(s)
    if sr[-1]==n:
        return sr[-2]
    else:
        return sr[-1]
	

for _ in range(t):
    # n = int(input())
    n,k = inp()

    if n<=k:
        print(1)
        continue

    if n%k==0:
        print(n//k)
    else:
        print(n//factor(n,k))
        # print(factor(n, k))

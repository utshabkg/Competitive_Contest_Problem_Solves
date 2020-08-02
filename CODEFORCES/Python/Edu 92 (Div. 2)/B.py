from __future__ import division, print_function
# import threading
# threading.stack_size(2**27)
# import sys
# sys.setrecursionlimit(10**7)
# sys.stdin = open('inpy.txt', 'r')
# sys.stdout = open('outpy.txt', 'w')
from sys import stdin, stdout
import bisect            #c++ upperbound
import math
import heapq
i_m=9223372036854775807
def inin():
    return int(input())
def stin():
    return input()
def spin():
    return map(int,stin().split())
def lin():                           #takes array as input
    return list(map(int,stin().split()))
def matrix(n):
    #matrix input
    return [list(map(int,input().split()))for i in range(n)]

################################################
def calculate_sum(a, N): #sum of a to N
    # Number of multiples 
    m = N / a 
    # sum of first m natural numbers 
    sum = m * (m + 1) / 2
    # sum of multiples 
    ans = a * sum
    return ans
def series(N):
    return (N*(N+1))//2

def count2Dmatrix(i,list):
    return sum(c.count(i) for c in list)

def modinv(n,p):
    return pow(n,p-2,p)

def GCD(x, y): 
    x=abs(x)
    y=abs(y)
    if(min(x,y)==0):
        return max(x,y)
    while(y): 
        x, y = y, x % y 
    return x
def LCM (x, y):
    return (x * y) // GCD(x, y)
    
def Divisors(n) : 
    l = []  
    for i in range(1, int(math.sqrt(n) + 1)) :
        if (n % i == 0) : 
            if (n // i == i) : 
                l.append(i) 
            else : 
                l.append(i)
                l.append(n//i)
    return l
def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
prime=[]
def SieveOfEratosthenes(n): 
    global prime
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    f=[]
    for p in range(2, n): 
        if prime[p]: 
            f.append(p)
    return f
q=[]       
def dfs(n,d,v,c):
    global q
    v[n]=1
    x=d[n]
    q.append(n)
    j=c
    for i in x:
        if i not in v:
            f=dfs(i,d,v,c+1)
            j=max(j,f)
            # print(f)
    return j
# d = {}
 
"""*******************************************************"""
for _ in range(inin()):
    n, k, z =spin()
    a = lin()
    s , ans, mx = 0, 0, 0

    for i in range(k+1):
        if i<n-1:
            mx = max(mx, a[i]+a[i+1])
        s += a[i]

        if i%2== k%2:
            temp = (k - i)//2
            if temp <= z:
                ans = max(ans, s + mx *temp)
    
    print(ans)


    # mx, index, temp = 0, 0, 0; j = 0

    # for i in range(n-1):
    #     temp = a[i]+a[i+1]
    #     j += 1
    #     if temp>mx:
    #         mx = temp
    #         index = j
    #     s.append(a[i]+a[i+1])
    # print(s, mx, index)

    # sm = 0
    # if index<=k:
    #     sm += sum(a[:index])
    #     k -= index
    
    # if k==0:
    #     print(sm)
    #     continue

    # if z==0:
    #     sm += sum(a[index:index+k+1])
    #     print(sm)
    #     continue
    # # print(sm)
    # l, r = 0, 0
    # if a[index-1-1]>a[index+1-1]:
    #     print(sm, 1)
    #     if k%2!=0:
    #         l, r = k//2 + 1, k//2 
    #     else:
    #         l, r = k//2, k//2
    #     sm += a[index-1-1] * l
    #     k -= (l - z)
    #     if l-z==0:
    #         sm += a[index-1] * r
    #     else:
    #         sm += a[index-1:index-1+(l-z)]
    # else:
    #     print(sm, 2, k)
    #     if k%2!=0:
    #         l, r = k//2, k//2 + 1 
    #     else:
    #         l, r = k//2, k//2
    #     sm += a[index-1] * l
    #     k -= l
    #     l -= z

    #     if l!=0:
    #         sm += 

    #     if k!=0:
    #         sm += sum(a[index+1-1:index+1-1+k])
        
    # print(sm)

    
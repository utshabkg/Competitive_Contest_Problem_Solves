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
    n = inin()
    a  = lin()

    c0, c1 = a.count(0), a.count(1)
    if c1<=n//2:
        print(c0)
        print(*[0]*c0)
    else:
        if c1%2!=0:
            print(c1-1)
            print(*[1]*(c1-1))
        else:
            print(c1)
            print(*[1]*c1)



    # even, odd = 0, 0; b = []
    # for i in range(n):
    #     if a[i]==1:
    #         if i%2!=0:
    #             even+=1
    #         else:
    #             odd+=1
        
    # if even==odd:
    #     print(n)
    #     print(*a)
    # else:
    #     # print(n - abs(even-odd), 2)
    #     j = abs(even-odd)
    #     if even>odd:
    #         for i in range(n):
    #             if j==0:
    #                 b.append(a[i])
    #                 continue
    #             if a[i]==1:
    #                 if i%2==0:
    #                     b.append(a[i])
    #                     j -= 1
    #             else:
    #                 b.append(a[i])
    #     else:
    #         for i in range(n):
    #             if j==0:
    #                 b.append(a[i])
    #                 continue
    #             if a[i]==1:
    #                 if i%2!=0:
    #                     b.append(a[i])
    #                     j -= 1
    #             else:
    #                 b.append(a[i])
    #             # j -= 1
    #     print(len(b))
    #     print(*b)




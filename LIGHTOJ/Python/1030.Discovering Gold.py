from __future__ import division, print_function
from sympy import symbols, Eq, solve
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
#######################################
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
def gcd(x ,y):
    while(y):
        t = x % y
        x = y
        y = t
    
    return x
# d = {}
 
"""*******************************************************"""
for t in range(1,inin()+1,1):
    n = inin()
    l = lin()
    l.insert(0, 0)
    # print(l)
    E = [0]*(n+1)

    k = 1
    for i in range(n-1,0,-1):
        for j in range(i+1,i+7,1):
            if j>n:
                break
            E[i] += l[j]+E[j]
        if n>6:
            if n-i<6:
                E[i] /= (6 - i + 2)
            else:
                E[i] /= 6
        else:
            E[i] /= k
            k+=1



        # if n-i<6:
        #     for j in range(n,i,-1):
        #         E[i] += l[j]+E[j]
        #     E[i] /= (6 - i + 2)
        # else:
        #     for j in range(i+1,i+7,1):
        #         if j>n:
        #             break
        #         E[i] += l[j]+E[j]
        #     E[i] /= 6
        print(i, l[i], E[i])
    
    print(E[1] + l[1])
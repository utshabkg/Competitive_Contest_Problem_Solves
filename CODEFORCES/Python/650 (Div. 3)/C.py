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
    n, k = spin()
    s = list(stin())

    # c = 0; temp = 0; t = 0; i = 0
    l = []; p = -1
    for i in range(n):
        if s[i]=='1':
            if p==-1 or i>p+k:
                p = i
            else:
                l.pop()
                p = i
        else:
            if i==0 or i>p+k:
                l.append(i)
                p = i

    # while i<n:
    #     if s[i]=='1':
    #         temp = 0
    #         i = i+k
    #     else:
    #         if i-k<0:
    #             if (s[i:i+k+1].count('1')==0 and s[0:i].count('1')==0):
    #                 s[i]='1'
    #                 temp = 0
    #                 c += 1
    #             i = i+k
    #                 # continue
    #         else:
    #             if (s[i:i+k+1].count('1')==0 and s[i-k:i].count('1')==0):
    #                 s[i]='1'
    #                 temp = 0
    #                 c += 1
    #             i = i+k

        
    print(len(l))

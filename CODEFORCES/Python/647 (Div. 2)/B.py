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
############################################
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
    l = [0]*1025

    def check(k):
        for i in range(1, n+1, 1):
            if not l[i] ^ k:
                return False
        return True

    def solve():
        booler = [False]*1025

        for i in range(1, n+1, 1):
            l[i] = 
            booler[l[i]] = True
        
        for i in range(1, 1024, 1):
            if check(k):
                print(k)
                return
        
        print(-1)
    
    solve()

    

    




    


# def bin2dec(n): 
#     return int(n,2)


# for _ in range(inin()):
#     n = inin()
#     l = lin()

#     new = []

#     m = max(l)
#     # print(m)
#     mb = bin(m).replace("0b","")
#     mblen = len(mb)

#     if l.count(0)>=1:
#         if len(set(l))==2:
#             print(m)
#             continue

#     # print(len(set(l)), l.count(0))

#     k = [0]*(mblen-2)
#     k.insert(0,1)
#     k = str("".join(map(str, k)))
#     # print(k)

#     for i in l:
#         xor = bin(bin2dec(bin(i).replace("0b","")) ^ bin2dec(k))
#         new.append(bin2dec(xor.replace("0b","")))
    
#     if sorted(l) == sorted(new):
#         print(bin2dec(k))
#     else:
#         print(-1)
#     # print(type(new.sort()))
#     # print(l.sort()==new.sort())

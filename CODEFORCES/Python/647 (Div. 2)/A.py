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
# d = {}
 
"""*******************************************************"""
for _ in range(inin()):
    a, b = spin()

    c = 0;flag = 0

    if a==b:
        print(0)
    elif a%2!=0 and b%2!=0:
        print(-1)
    elif max(a,b)%min(a,b)!=0:
        print(-1)
    else:
        q = max(a,b)//min(a,b)
        p = math.log10(q) // math.log10(2)
        eight = p//3;p=p%3
        four = p//2;p=p%2
        two = p//1

        # if a>b:
        #     while True:
        #         if a%8==0:
        #             a=a//8
        #             c+=1
        #         elif a%4==0:
        #             a=a//4
        #             c+=1
        #         elif a%2==0:
        #             a=a//2
        #             c+=1
        #         if a==b:
        #             break
        #         # if a<b:
        #         #     print(-1)
        #         #     flag = 1
        #         #     break
        # else:
        #     while True:
        #         if b%8==0:
        #             b=b//8
        #             c+=1
        #         elif b%4==0:
        #             b=b//4
        #             c+=1
        #         elif b%2==0:
        #             b=b//2
        #             c+=1
        #         if a==b:
        #             break
        #         # if a>b:
        #         #     print(-1)
        #         #     flag = 1
        #         #     break
        print(int(eight + four + two))

# print(1100611139403776/1001)
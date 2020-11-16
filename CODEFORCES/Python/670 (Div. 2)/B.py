<<<<<<< HEAD
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
    A = lin()

    A.sort()
    x=A[n-5]*A[n-4]*A[n-3]*A[n-2]*A[n-1]
    y=A[0]*A[1]*A[n-3]*A[n-2]*A[n-1]
    z=A[0]*A[1]*A[2]*A[3]*A[n-1]

    print(max(x,y,z))

    # n, p = [], []; m = 1
    # for i in a:
    #     if i<0:
    #         n.append(i)
    #     else:
    #         p.append(i)

    # a.sort();n.sort();p.sort()[::-1]
    # l = 0; r = len(a)-1; flag = 0

    # for i in range(5):

    #     temp = (abs(a[l]), abs(a[r]))
            
    #     if temp < 0:
    #         if c==0:
    #             if len(n)>=2:
    #                 m *= temp
    #         elif c==2:
    #             if len(n)>=4:
    #                 m *= temp
=======
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
    A = lin()

    A.sort()
    x=A[n-5]*A[n-4]*A[n-3]*A[n-2]*A[n-1]
    y=A[0]*A[1]*A[n-3]*A[n-2]*A[n-1]
    z=A[0]*A[1]*A[2]*A[3]*A[n-1]

    print(max(x,y,z))

    # n, p = [], []; m = 1
    # for i in a:
    #     if i<0:
    #         n.append(i)
    #     else:
    #         p.append(i)

    # a.sort();n.sort();p.sort()[::-1]
    # l = 0; r = len(a)-1; flag = 0

    # for i in range(5):

    #     temp = (abs(a[l]), abs(a[r]))
            
    #     if temp < 0:
    #         if c==0:
    #             if len(n)>=2:
    #                 m *= temp
    #         elif c==2:
    #             if len(n)>=4:
    #                 m *= temp
>>>>>>> b7522ba5389778e8576c407c6c561f68ab2635c7
    #     flag = 1
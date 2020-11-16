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
def string2intlist(s):
    return list(map(int, s))

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

n = inin()
l = lin()
if n==1:
    print(1,1)
    print(-l[0])
    print(1,1)
    print(0)
    print(1,1)
    print(0)
else:
    print(1,n)
    print(' '.join([str(-n*i) for i in l]))
    print(1,n-1)
    print(' '.join([str((n-1)*i) for i in l[:n-1]]))
    print(2,n)
    print(' '.join([str(0) for i in range(n-2)]+[str((n-1)*l[-1])]))
# print(1,1)
# print(-a[0])
# 
# b = []; c = []
# print(3, n)
# 
# m = (n-2)+1
# for i in range(2, n):
#     b.append((m-1)*a[i])
#     a[i] = (m-1)*a[i]+ a[i]
# 
#     c.append(-a[i])
# 
# print(*b)
# for i in range(1, n):
#     print(i+1, end=" ")
# print(2,n)
# print(*c)
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
def string2intlist(s):
    return list(map(int, s))

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

n = inin()
a = lin()

print(1,1)
print(-a[0])

b = []; c = []
print(3, n)

m = (n-2)+1
for i in range(2, n):
    b.append((m-1)*a[i])
    a[i] = (m-1)*a[i]+ a[i]

    c.append(-a[i])

print(*b)
# for i in range(1, n):
#     print(i+1, end=" ")
print(2,n)
print(*c)
>>>>>>> b7522ba5389778e8576c407c6c561f68ab2635c7

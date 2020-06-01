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
for i in range(int(input())):
    s=input();t=10**18
    for j in range(len(s)):
        a=s[:j].count('1');b=s[:j].count('0')
        c=s[j:].count('1');d=s[j:].count('0')
        t=min(t,b+c,a+d)
    print(t)




# for _ in range(inin()):
#     l = list(stin())

#     num0, num1 = l.count('0'), l.count('1')

#     done0, done1 = 0, 0

#     # ans1, ans2 = 0, 0

#     for i in range(1,len(l),1):
#         if l[0]=='0':
#             done0+=1
#             ans1 = done0 + num1 - done1
#         elif l[0]=='1':
#             done1+=1
#             ans2 = done1 + num0 - done0

#     print(min(ans1, ans2))




#     # c = 0
#     # f0, f1 = 0, 0

#     # for i in range(1,len(l),1):
#     #     if l[0]=='0' and i<len(l):
#     #         if l[i]=='1':
#     #             f0=1
#     #         if l[i]=='0' and f0==1:
#     #             f1=1
#     #     if l[0]=='1' and i<len(l):
#     #         if l[i]=='0':
#     #             f0=1
#     #         if l[i]=='1' and f0==1:
#     #             f1=1
#     #     # print(f0, f1)
#     # if f1==0:
#     #     print(0)
#     # else:
#     #     if l[0]==l[-1]:
#     #         del l[0]; 
#     #         if len(l)!=0:
#     #             del l[-1]
#     #         if l.count('0')!=0 and l.count('1')!=0:
#     #             print(min(l.count('0'), l.count('1')))
#     #         elif l.count('0')==0:
#     #             print(l.count('1'))
#     #         elif l.count('1')==0:
#     #             print(l.count('0'))
        
#     #     else:
#     #         del l[0];
#     #         if len(l)!=0:
#     #             del l[-1]
#     #         print(min(l.count('0'), l.count('1')))
        
    
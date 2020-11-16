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
    a = lin()

    mx =max(a)
    ans = ['a' * (mx+1)] * (n+1)

    for i, x in enumerate(a):
        temp ='a' if ans[i][x]=='b' else 'b'
        ans[i+1] = ans[i][:x] + temp + ans[i][x+1:]
    print('\n'.join(ans))
    # # for i in range(len(a)):
    # #     if a[i]==0:
    # #         if i>0 and a[i-1]==0:
    # #             if i%2!=0:
    # #                 print('x')
    # #             else:
    # #                 print('y')
    # #             continue
    # #         elif a[i-1]>0:
    # #             print("".join(['a']*a[i-1]))
    # #             continue
    # #         elif i==0:
    # #             if i%2!=0:
    # #                 print('x')
    # #             else:
    # #                 print('y')
    # #             continue
    # #     if i==0:
    # #         print("".join(['a']*a[i]))
    # #     else:
    # #         if a[i-1]<=a[i]:
    # #             print("".join(['a']*a[i]))
    # #         else:
    # #             print("".join(['a']*a[i-1]))
    # # if a[n-1]!=0:
    # #     print("".join(['a']*a[n-1]))
    # # else:
    # #     print('z')

    # temp ='x'
    # for i in range(n):
    #     if i==0:
    #         if a[i]==0:
    #             if i+1<n:
    #                 print('x')
    #                 if a[i+1]>0:
    #                     print("".join(['b']*a[i+1]), 1)
    #                     temp = "".join(['b']*a[i+1])
    #                 else:
    #                     print("".join(['b']*1))
    #                     temp = "".join(['b']*1)
    #             else:
    #                 print('x')
    #                 print("".join(['b']*1), 2)
    #                 temp = "".join(['b']*1)
    #         else:
    #             print("".join(['a']*a[i]))
    #             print("".join(['a']*a[i]), 3)
    #             temp = "".join(['a']*a[i])
    #             # print("t", temp)
    #     else:
    #         if a[i]==0:
    #             if temp == "".join(['a']*a[i-1]):
    #                 if i+1<n:
    #                     if a[i+1]>0:
    #                         print("".join(['b']*a[i+1]), 4)
    #                         temp = "".join(['b']*a[i+1])
    #                     else:
    #                         print("".join(['b']*1), 5)
    #                         temp = "".join(['b']*1)
    #                 #     print("".join(['b']*a[i+1]), 4)
    #                 #     temp = "".join(['b']*a[i+1])
    #                 # else:
    #                 #     print("".join(['b']*1), 5)
    #                 #     temp = "".join(['b']*1)
    #             else:
    #                 if i+1<n:
    #                     print("".join(['a']*a[i+1]), 6)
    #                     temp = "".join(['a']*a[i+1])
    #                 else:
    #                     print("".join(['a']*a[i]), 7)
    #                     temp = "".join(['a']*a[i])
    #         else:
    #             print(temp, 8)
        

    # temp = ['a']; temp2 = ['a']
    # for i in range(n):
    #     if a[i]==0:
    #         if i+1<n:
    #             if a[i+1]==0:
    #                 print("".join(temp * 1))
    #             else:
    #                 print("".join(temp * a[i+1]))
    #             if a[i+1]==0:
    #                 if temp==['a']:
    #                     temp = ['b']
    #                 else:
    #                     temp =['a']
    #         else:
    #             print('x')
    #     else:
    #         if i==0:
    #             print("".join(temp2*a[i]))
    #         elif i+1<n and i!=0:
    #             if a[i+1]>a[i]:
    #                 print("".join(temp*a[i+1]))
    #             else:
    #                 print("".join(temp*a[i]))
    #         else:
    #             print("".join(temp*a[i]))
    #         if i+1<n:
    #             if a[i+1]==0:
    #                 if temp==['a']:
    #                     temp = ['b']
    #                 else:
    #                     temp =['a']
                    
        
    #     if i==0:

    #         if a[i]==0:
    #             if i+1<n:
    #                 if a[i+1]==0:
    #                     print("".join(temp * 1))
    #                     if temp==['a']:
    #                         temp = ['b']
    #                     else:
    #                         temp =['a']
    #                 else:
    #                     print("".join(['b'] * a[i+1]))
    #                     temp = ['b']
                    
    #         else:
    #             if i+1<n:
    #                 if a[i+1]>a[i]:
    #                     print("".join(temp2*a[i+1]))
    #                 else:
    #                     print("".join(temp2*a[i]))



                
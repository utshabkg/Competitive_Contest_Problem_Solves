from __future__ import division, print_function
# import threading
# threading.stack_size(2**27)
# import sys
# sys.setrecursionlimit(10**7)
# sys.stdin = open('inpy.txt', 'r')
# sys.stdout = open('outpy.txt', 'w')
from sys import stdin, stdout
import bisect  # c++ upperbound
import math
import heapq
i_m = 9223372036854775807


def inin():
    return int(input())


def stin():
    return input()


def spin():
    return map(int, stin().split())


def lin():  # takes array as input
    return list(map(int, stin().split()))


def matrix(n):
    #matrix input
    return [list(map(int, input().split()))for i in range(n)]

################################################


def count2Dmatrix(i, list):
    return sum(c.count(i) for c in list)


def modinv(n, p):
    return pow(n, p - 2, p)


def nCr(n, r):
    i = 1
    while i < r:
        n *= (n - i)
        i += 1
    return n // math.factorial(r)


def GCD(x, y):
    x = abs(x)
    y = abs(y)
    if(min(x, y) == 0):
        return max(x, y)
    while(y):
        x, y = y, x % y
    return x


def Divisors(n):
    l = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n // i == i):
                l.append(i)
            else:
                l.append(i)
                l.append(n//i)
    return l


prime = []


def SieveOfEratosthenes(n):
    global prime
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    f = []
    for p in range(2, n):
        if prime[p]:
            f.append(p)
    return f


q = []


def dfs(n, d, v, c):
    global q
    v[n] = 1
    x = d[n]
    q.append(n)
    j = c
    for i in x:
        if i not in v:
            f = dfs(i, d, v, c+1)
            j = max(j, f)
            # print(f)
    return j
# d = {}


"""*******************************************************"""

for _ in range(inin()):
    n = inin()
    # s = stin()

    s = ''; flag = -1
    # for i in range(10 ** 9):
    #     s = list(str(i))
    #     print(s)
    #     if set(s) == s and sum(int(s)) == x:
    #         print(int(s))
    #         break
    #     else:
    #         flag =-1
    # if flag == -1:
    #     print(flag)

    if n <= 9:
        print(n)
    elif n < 18:
        for i in range(1, 9):
            if i + 9 == n:
                print(str(i) + '9')
                break
    elif n <= 24:
        for i in range(1, 9):
            if i + 8 + 9 == n:
                print(str(i) + '89')
                break

    elif n <= 30:
        for i in range(1, 9):
            if i + 7+ 8 + 9 == n:
                print((str(i) + '789'))
                break
    elif n <= 35:
        for i in range(1, 9):
            if i + 6 + 7 + 8+ 9 == n:
                print((str(i) + '6789'))
                break

    elif n <= 39:
        for i in range(1, 9):
            if i + 5 + 6 + 7 + 8 + 9 == n:
                print((str(i) + '56789'))
                break
    elif n <= 42:
        for i in range(1, 9):
            if i + 4 + 5 + 6 + 7 + 8 + 9 == n:
                print((str(i) + '456789'))
                break
    elif n <= 44:
        for i in range(1, 9):
            if i + 3 + 4 + 5 + 6 + 7 + 8 + 9 == n:
                print((str(i) + '3456789'))
                break
    elif n == 45:
        print(123456789)
    else:
        print(-1)
    
            


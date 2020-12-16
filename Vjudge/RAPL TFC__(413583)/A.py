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

n = inin()

# a = 2 ** n
# print(a % 1000000007)
# ans = (a*(a+1)) % 1000000007
# print(ans // 2)

def modularExponentiation(x, n):
    M = 10**9+7
    if(n == 0):
        return 1
    elif (n % 2 == 0): # n is even
        return modularExponentiation((x*x) % M, n//2)
    else: # n is odd
        return (x * modularExponentiation((x * x) % M, (n - 1) // 2)) % M

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

a = modularExponentiation(2, n)
b = (modularExponentiation(2, n) + 1 % (10**9+7)) % (10**9+7)
# print(a)
ab = ((a * b) % (10 ** 9 + 7))
r = ((ab % (10**9+7)) * modInverse(2, (10**9+7))) % (10**9+7)
print(r)

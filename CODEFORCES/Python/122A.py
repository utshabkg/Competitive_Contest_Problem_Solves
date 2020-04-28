import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
 
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
 
def MI(): return map(int, sys.stdin.readline().strip().split())
def LI(): return list(map(int, sys.stdin.readline().strip().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines().strip()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().strip().split()]
def LF(): return [float(x) for x in sys.stdin.readline().strip().split()]
def LS(): return sys.stdin.readline().strip().split()
def I(): return int(sys.stdin.readline().strip())
def F(): return float(sys.stdin.readline().strip())
def S(): return sys.stdin.readline().strip()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)
 
from math import factorial,gcd
from random import choice,randint
from sys import stdin,stdout 
inp=stdin.readline
out=stdout.write
 
def main():
    l = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    n = I()
    for i in l:
        if n%i==0:
            print("YES")
            break
    else:
        print("NO")

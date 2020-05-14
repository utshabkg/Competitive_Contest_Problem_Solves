import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
 
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

n, t=map(int,input().split())
s = list(input())

for i in range(0, t):
    for j in range(0, n):
        print(j)
        if s[j]=="B" and s[j+1]=="G":
            s[j]="G"
            s[j+1]="B"
            print(s)
        if j==n-2:
            break
    print(s)

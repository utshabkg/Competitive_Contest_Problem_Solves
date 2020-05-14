import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
 
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]



for i in range(int(input())):
    x, y=map(int,input().split())
    a, b=map(int,input().split())

    c1= 0;c2=0

    c1 = int(math.fabs(x-y))
    c2 = min(x,y)
    print(min(a*(x+y), c1*a+c2*b))




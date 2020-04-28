import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
 
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


for i in range(int(input())):
	s = input()

	if len(set(s))==1:
		print(s)
		continue
	print("01"*len(s))
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

inp=lambda:map(int,input().split())
n = int(input())
l = list(inp())

if max(l)!=min(l):
    print(max(l)-min(l), l.count(max(l)) * l.count(min(l)))
else:
    print(max(l)-min(l), int(ncr(l.count(max(l)), 2)))

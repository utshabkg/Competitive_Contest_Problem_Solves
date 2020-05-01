from math import gcd

inp=lambda:map(int,input().split())

def solve(row):
    N = len(row)
    row1 = []
    for i in range(1, N):
        if row[i] != row[i - 1]:
            row1.append(abs(row[i] - row[i - 1]))
    g = row1[0]
    for e in row1:
        g = gcd(g, e)
    return g

while True:
    l=list(inp())
    if l[0] == 0:
        break
    l.pop()
    print(solve(l))
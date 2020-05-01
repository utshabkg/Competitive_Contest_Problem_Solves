i=lambda:map(int,input().split())

n = int(input())
c=0

for _ in range(n):
    p, q = i()
    if q-p >=2:
        c += 1

print(c)
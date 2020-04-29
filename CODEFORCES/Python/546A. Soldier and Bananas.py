i=lambda:map(int,input().split())

k, n, w = i()

total = 0

for i in range(1,w+1):
    total = total + i*k

if total-n <=0:
    print(0)
else:
    print(total - n)
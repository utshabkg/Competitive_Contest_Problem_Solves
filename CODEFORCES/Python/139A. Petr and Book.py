i=lambda:map(int,input().split())
n = int(input())
l=list(i())

c = 0

while True:
    if n<=0:
        break
    j = 0
    for j in range(7):
        if n<=0:
            c = j
            break
        else:
            n = n - l[j]
if c==0:
    print(7)
else:
    print(c)

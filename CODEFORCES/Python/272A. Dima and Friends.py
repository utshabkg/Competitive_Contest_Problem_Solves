i=lambda:map(int,input().split())

n = int(input())
l = list(i())

s = sum(l)

T,c = 0, 0
while T>=0:
    if T!=0 and s%(n+1)==0 and c!=1:
        break
    else:
        s = s + 1
        c = c + 1
    T = T + 1

if c>5:
    print(c%5)
else:
    print(c)
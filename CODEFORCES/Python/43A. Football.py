n = int(input())

c1, c2 = 0, 0

for i in range(n):
    s = input()
    if i==0:
        t1 = s
        c1 += 1
    elif i>0 and t1!=s:
        t2 = s
        c2 += 1
    else:
        t1 = s
        c1 += 1

if c1>c2:
    print(t1)
else:
    print(t2)
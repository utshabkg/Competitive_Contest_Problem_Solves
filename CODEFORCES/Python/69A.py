n = int(input())
s=[0,0,0]

for i in range(n):
    a = input().split(' ')
    s[0] = s[0] + int(a[0])
    s[1] = s[1] + int(a[1])
    s[2] = s[2] + int(a[2])
    

if (s[0], s[1], s[2]) ==(0,0,0):
    print('YES')
else:
    print('NO')

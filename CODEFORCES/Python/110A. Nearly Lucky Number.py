n = int(input())

s = str(n)
c = 0

for i in range(len(s)):
    if s[i]=='4' or s[i]=='7':
        c += 1

if c==4 or c==7:
    print("YES")
else:
    print("NO")
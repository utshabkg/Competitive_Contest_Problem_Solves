s = input()

u, l = 0,0

for i in range(len(s)):
    if s[i].islower():
        l += 1
    else:
        u += 1

if u==l or u<l:
    print(s.lower())
else:
    print(s.upper())
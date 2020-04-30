s = input()

flag = 0

if s[0].isupper():
    for i in range(1, len(s)):
        if s[i].islower():
            flag = 0
            break
        else:
            flag = 1

elif s[0].islower():
    for i in range(1, len(s)):
        if s[i].islower():
            flag = 0
            break
        else:
            flag = 2

if flag == 0 and len(s)!=1:
    print(s)
elif len(s)==1 and s[0].islower():
    print(s.title())
elif len(s)==1 and s[0].isupper():
    print(s.lower())
elif flag == 1:
    print(s.lower())
else:
    print(s.title())

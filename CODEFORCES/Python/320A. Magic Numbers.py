s = input()
flag = 0
for i in range(0,len(s)):
    if s[0]!='1':
        flag = 0
        break
    if s[i]!='1' and s[i]!='4':
        flag = 0
        break
    if s[i]=='1':
        flag = 1
        continue

    if s[i]=='4' and i>0:
        if s[i-1]=='1':
            flag = 1
            continue
        elif s[i-1]=='4' and s[i-2]=='1':
            flag = 1
            continue
        else:
            flag = 0
            break

if flag==1:
    print("YES")
else:
    print("NO")
            
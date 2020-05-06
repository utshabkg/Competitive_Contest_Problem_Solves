s = input()
flag = 1

for i in range(len(s)):
    if s[0]!='1':
        flag = 0
        # print(flag)
        break
    if s[i]!='1' or s[i]!='4':
        flag = 0
        break

    if s[i]=='1':
        flag = 1
        # print(flag)
        continue
    if s[i]=='4' and i>0:
        if s[i-1]=='1':
            flag = 1
            # print(flag)
            continue
        elif s[i-1]=='4' and s[i-2]=='1':
            flag = 1
            # print(flag)
            continue
    # print(flag)

if flag==1:
    print("YES")
else:
    print("NO")
            
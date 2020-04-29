s = input()

sh = 'hello'
c = 0

for i in range(len(s)):
    if c<5:
        if s[i]==sh[c]:
            c+=1

if c==5:
    print("YES")
else:
    print("NO")

# import re
# print("YES"if re.search("h.*e.*l.*l.*o",input())else"NO")
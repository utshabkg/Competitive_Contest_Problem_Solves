n = int(input())

flag = 0

for i in[4,7,47,74,44,444,447,474,477,777,774,744]:
    if(n%i==0):
        flag = 1
        break
    else:
        flag = 0

if flag==1:
    print("YES")
else:
    print("NO")
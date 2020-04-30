s = input()
flag = 0

# "H" prints "Hello, World!",
# "Q" prints the source code of the program itself,
# "9" prints the lyrics of "99 Bottles of Beer" song,
# "+" increments the value stored in the internal accumulator.

for i in range(len(s)):
    if s[i]=='H' or s[i]=='Q' or s[i]=='9': #or s[i]=='+':
        flag = 1
        break


if flag == 1:
    print("YES")
else:
    print("NO")
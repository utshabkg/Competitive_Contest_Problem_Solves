inp = input()
s = list(inp)
l = []
max = 0

s.append('A')

# print(s)
# print(len(s))

for i in range(0, len(s), 1):
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='Y':
        l.append(i+1)
    
# print(l)

max = l[0]
for j in range(len(l)):
        
    if j+1==len(l):
        break
    d = l[j+1]-l[j]
    if(d>max):
        max = d

print(max)
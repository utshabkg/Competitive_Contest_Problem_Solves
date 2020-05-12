inp=lambda:map(int,input().split())

l = list(inp())
s = input()

dx = l[3] - l[1]
dy = l[4] - l[2]
count = 0

for i in range(l[0]):
    if dx==0 and dy==0:
        break
    if dx < 0:
        if s[i]=='W':
            dx += 1
        
    elif dx > 0:
        if s[i]=='E':
            dx -= 1
            
    if dy < 0:
        if s[i]=='S':
            dy += 1
        
    elif dy > 0:
        if s[i]=='N':
            dy -= 1
    count += 1
    # print(i,count,dx, dy)

if dx==0 and dy==0:
        print(count)
else:
    print(-1)
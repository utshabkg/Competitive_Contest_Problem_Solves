inp=lambda:map(int,input().split())
t = int(input())
l = list(inp())

s = sorted(l)
sr = s[::-1]

sum,count = 0, 0

for i in range(0,12):
    if sum>=t:
        break
    else:
        sum += sr[i]
        count += 1
        continue
if t>sum:
    print(-1)
else:
    print(count)
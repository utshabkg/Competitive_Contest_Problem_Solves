import math
inp=lambda:map(int,input().split())

n = int(input())
l = list(inp())

sr = sorted(l)
# print(sr)

if len(sr)==1:
    print(1)
    exit()
if sr[0]==sr[1]:
    print("Still Rozdil")
    exit()

minm = l[0]
city = 0

for i in range(n):
    if l[i] < minm:
        minm = l[i]
        city = i

print(city+1)
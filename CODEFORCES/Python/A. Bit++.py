#n = int(input().rstrip())
# 
#x = 0
 
#for i in range(n):
#    x += (1 if '+' in input() else -1)
 
#print(x)

TN = 1
def solution():
    n = int(input())
    ans = 0
    for i in range(n):
        l = input()
        if "+" in l: ans += 1
        else: ans -= 1
    print(ans)

while TN != 0:
    solution()
    TN -= 1

# NOT solved yet
inp=lambda:map(int,input().split())
n = int(input())
s = input()

sr = sorted(list(set(s)))
sr2 = "".join(sr)
flag = 1
for i in range(len(sr)):
    if i+1==len(sr):
        break
    if s.count(sr[i])==s.count(sr[i+1]):
        print(s.count(sr[i]))
        flag = 1
    else:
        flag = 0

if flag==0:
    print(-1)
    exit()
l = []
for i in range(s.count(sr[0])):
    l.append(sr2)

print("".join(l))
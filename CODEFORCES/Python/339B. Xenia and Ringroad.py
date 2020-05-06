inp=lambda:map(int,input().split())
n,k=inp()
l=list(inp())

time = 0

for i in range(k):
    if i==0:
        time = time + l[i] - 1
    if i!=0 and l[i-1]>l[i]:
        time += n - l[i-1] + l[i]
        # print(i+1,":",time)
        continue
    elif i!=0 and l[i-1]<l[i]:
        time = time + l[i] - l[i-1]
    else:
        pass
    # print(i+1,":",time)
    # if sr[i]==sr[i+1]:
    #     time+=0
    # else:

print(time)
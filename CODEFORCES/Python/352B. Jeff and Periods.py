## NOT solved yet

inp=lambda:map(int,input().split())
n = int(input())
l = list(inp())

sr = sorted(list(set(l)))
index=[]

for i in sr:
    count = 0
    temp = 0
    for j in range(n):
        if i==l[j]:
            if count==0:
                count += 1
                continue
            if count==1:
                temp = j - temp
                count += 1
                continue
            if count!=0 and j-temp!=temp:
                count = -100
                break
            # else:
            #     temp = j - temp
            #     count += 1
            
        # if count==0 and i==l[j]:
        #     temp = j
        #     count += 1
        #     continue
        # if count!=0 and i==l[j]:
        #     temp = j - temp
        #     count += 1
        #     break
    if count!=-100:
        index.append(temp)
    
    print(len(index))
    
    if count==1:
        print(i, 0)
    elif count==-100:
        pass
    else:
        print(i, temp)


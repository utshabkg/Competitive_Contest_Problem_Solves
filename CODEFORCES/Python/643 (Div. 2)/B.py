import math

inp=lambda:map(int,input().split())
t = int(input())

for _ in range(t):
    n = int(input())
    # n,k = inp()
    l = list(inp())
    sr = sorted(l)

    count = 0; i = 0

    while i<n:
        if len(sr)<sr[0]:
            break
        if i==0:
            count+=sr.count(i+1)
            sr = [x for x in sr if x != i+1]
            if len(sr)==0:
                break
            sr = sr[::-1]
            i=sr[0]
            # print(i,sr)
            continue

        if len(sr)>=i:
            count += 1
            del sr[0:i]
            if len(sr)==0:
                break
            i = sr[0]
        # print(sr)
        # else:
        #     if len(sr)!=0:
        #         count += sum(sr)/len(sr)
        #     break
    # else:
        # if sr.count(i+2)>=2:
        # else:
        #     if i==n-2:
        #         break
        #     count+=sr.count((i+1))//(i+1)
        #     if sr.count((i+1))/(i+1) - (i+1)>0:
        #         sr = [x for x in sr if x != i+2]
        #         sr.insert(0, i+1)
        #     elif sr.count((i+1))/(i+1) - (i+1)==0:
        #         sr = [x for x in sr if x != i+2]

        #     if i==n-3:
        #         break
        #     if sr.count(i+1)+sr.count(i+2) >= sr.count(i+2):
        #         if sr.count(i+2) >= (i+2):
        #             count+=sr.count((i+2))//(i+2)
        #         else:
        #             count+=sr.count((i+2))//(i+2) + 1
        #     if sr.count((i+2)/(i+2)) - (i+2)>0:
        #         sr.remove(i+2)
        #         sr.insert(0, i+2)
            
        #     if i==n-4:
        #         break
        #     count+=sr.count((i+3))//(i+3)
        #     if sr.count((i+3)/(i+3)) - (i+3)>0:
        #         sr.remove(i+3)
        #         sr.insert(0, i+3)
            
        #     if i==n-5:
        #         break
        #     count+=sr.count((i+4))//(i+4)
        #     if sr.count((i+4)/(i+4)) - (i+4)>0:
        #         sr.remove(i+4)
        #         sr.insert(0, i+4)
        # i+=5
    print(count)



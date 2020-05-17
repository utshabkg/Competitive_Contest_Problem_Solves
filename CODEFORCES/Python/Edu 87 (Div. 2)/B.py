inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    s = input()

    # temp1, temp2, temp3 = 0, 0, 0
    l1, l2, l3 = [], [], []
    c1, c2, c3 = 200000, 200000, 200000
    for i in range(len(s)):
        if s.count('1')==0 or s.count('2')==0 or s.count('3')==0:
            c1 = 0
            break
        
        # if i==0 and s[i]=='1':
        #     temp1+=1
        # elif i==0 and s[i]=='2':
        #     temp2+=1
        # elif i==0 and s[i]=='3':
        #     temp3+=1

        # if s[i]=='1':
        #     if temp1==0:
        #         temp1 += 1
        #     if s[i+1]=='2' and i<s-1:
        #         temp1+=1
        #         temp2+=1
        #     elif s[i+1]=='3' and i<s-1:
        #         temp1+=1
        #         # temp2+=1
        #         temp3+=1

        if s[i] == '1':
            if len(l1)==0:
                l1.append(s[i])
            if len(l2)>0:
                    l2.append(s[i])
            if len(l3)>0:
                l3.append(s[i])
            
        
        if s[i] == '2':
            if len(l2)==0:
                l2.append(s[i])
            if len(l1)>0:
                l1.append(s[i])
            if len(l3)>0:
                l3.append(s[i])
            
        if s[i] == '3':
            if len(l3)==0:
                l3.append(s[i])
            if len(l2)>0:
                    l2.append(s[i])
            if len(l1)>0:
                l1.append(s[i])


        # if s[i]=='1':
        #     if temp1==0:
        #         temp1 += 1
        #         l1.append(s[i])
        #     if i<len(s)-1:
        #         if s[i+1]!='1':
        #             temp1+=1
        #             l1.append(s[i])
        #             if temp2>0:
        #                 temp2 += 1
        #                 l2.append(s[i])
        #             if temp3>0:
        #                 temp3 += 1
        #                 l3.append(s[i])
        

        # elif s[i]=='2':
        #     if temp2==0:
        #         temp2 += 1
        #         l2.append(s[i])
        #     if i<len(s)-1:
        #         if s[i+1]!='2':
        #             temp2+=1
        #             l2.append(s[i])
        #             if temp1>0:
        #                 temp1 += 1
        #                 l1.append(s[i])
        #             if temp3>0:
        #                 temp3 += 1
        #                 l3.append(s[i])

        # elif s[i]=='3':
        #     if len(l3)==0:
        #         temp3 += 1
        #         l3.append(s[i])
        #     else:
        #         pass
            
        #     if i<len(s)-1:
        #         if s[i+1]!='3':
        #             temp3+=1
        #             l3.append(s[i]+1)
        #             if temp1>0:
        #                 temp1 += 1
        #                 l1.append(s[i]+1)
        #             if temp2>0:
        #                 temp1 += 1
        #                 l1.append(s[i]+1)
    
        if l1.count('1')>=1 and l1.count('2')>=1 and l1.count('3')>=1:
            if c1>len(l1):
                c1 = len(l1)
            l1 = []

        if l2.count('1')>=1 and l2.count('2')>=1 and l2.count('3')>=1:
            if c2>len(l2):
                c2 = len(l2)
            l2 = []

        if l3.count('1')>=1 and l3.count('2')>=1 and l3.count('3')>=1:
            if c3>len(l3):
                c3 = len(l3)
            l3 = []
        
        # print(temp1, temp2, temp3)
        # print(i, len(l1), len(l2), len(l3)) 
        # print(l1, l2, l3)
        # print(c1,c2,c3)

    print(min(min(c1, c2), c3))

    #12222133333332
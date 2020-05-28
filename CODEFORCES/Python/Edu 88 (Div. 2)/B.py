#multiple int & line of int
inp=lambda:map(int,input().split())
t = int(input())
for _ in range(t):
    n, m, x, y = inp()

    cost = 0;
    for i in range(n):
        # c = 0
        s = input()
        l=list(s)
        j = 0

        while j<len(l):
            # if len(l)==0 or l.count('.')==0:
            #     break
            
            if l[j]=='.':
                if j!=len(l)-1:
                    if l[j+1]=='.':
                        if 2*x>=y:
                            cost += y
                            # del l[j];del l[j]
                            j+=2
                        else:
                            cost += 2*x
                            # del l[j];del l[j]
                            j+=2
                    else:
                        cost += x
                        # del l[j]
                        j+=1
                else:
                    cost += x
                    # del l[j]
                    j+=1
            else:
                j+=1
    # print(cost)

                    
    print(cost)






    
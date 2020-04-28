x=int(input())
a = list(map(int, input().split()))
l = sorted(a)
print(l)
count = 0
vacancy = []

for i in range(x):
    if l[i]==4:
        count = count+1
        vacancy[i]=vacancy.append(0)
    else:
        for j in range(len(vacancy)):
            if vacancy[j] >= l[i]:
                vacancy[i] = vacancy[i] - l[i]
            else:
                vacancy[i] = 4 - l[i]
                count = count+1
print(count)
    
    

x = int(input())
l = input()
count = 0

for i in range(x):
    if i>0 and l[i] == l[i-1]:
        count = count + 1
        
print(count)

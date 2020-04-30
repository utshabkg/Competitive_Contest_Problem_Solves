i=lambda:map(int,input().split())
n,k=i()
s = input()
t = list(s)

for _ in range(k):
    j = 0
    while (j!=n):
        if(j==n-1):
            break
        if t[j] == 'B' and t[j+1]=='G':
            t[j] , t[j+1] = t[j+1], t[j]
            j = j+2
        else:
            j = j+1

# print(t)
print("".join(t))
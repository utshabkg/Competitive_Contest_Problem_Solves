inp=lambda:map(int,input().split())
n, m = inp()

for i in range(n):
    s = input()
    l=[]
    for j in range(len(s)):
        if s[j]=='-':
            l.append('-')
            continue
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
            l.append('B')
        if (i%2!=0 and j%2==0) or (i%2==0 and j%2!=0):
            l.append('W')
        
    print("".join(l))
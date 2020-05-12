n = int(input())

l = []
sr = []

for i in range(1,n+1):
        l.append(i)

        if i==n:
            sr = sorted(l)
            sr.insert(0, n)
            del sr[-1]

print(*sr)
t = int(input())

for i in range(t):
    a = int(input())
    for j in range(a, 2, -2):
        if a>11 and a!=j and a%j == 0:
            print(a//j)
            break
        elif a<11 and a%j==0:
            print(a//j)
            break
        else:
            pass

# 781241644, 381652
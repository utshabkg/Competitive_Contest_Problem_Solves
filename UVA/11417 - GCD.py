import math


while(0 or 1):
    try:
        num = int(input())
        G = 0
        if num == 0:
            break
        for i in range(1,num,1):
            for j in range(i+1, num+1,1):
                G = G + math.gcd(i,j)
        print(G)
    except EOFError:
        break

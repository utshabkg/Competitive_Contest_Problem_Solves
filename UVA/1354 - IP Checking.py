i=lambda:map(int,input().split("."))

T = int(input())

for j in range(1,T+1):
    d = list(i())
    b = list(i())
    
    if (str(bin(d[0]).replace("0b", "")))==str(b[0]) and str((bin(d[1]).replace("0b", "")))==str(b[1]) and str((bin(d[2]).replace("0b", "")))==str(b[2]) and str((bin(d[3]).replace("0b", "")))==str(b[3]):
        print("Case %d: Yes" %j)
    else:
        print("Case %d: No" %j)


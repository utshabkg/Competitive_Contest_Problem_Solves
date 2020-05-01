T = int(input())

i=lambda:map(int,input().split())

while T >0:
    n,k=i()
    l = list(i())
    if k%2!=0:
        
        if "".join(l)=="".join(reversed(str(l))):
            print(*l)
import math

i=lambda:map(int,input().split())

for _ in range(int(input())):
    g, l = i()
    
    if l%g:
        print("-1")
    else:
        print(g,l)
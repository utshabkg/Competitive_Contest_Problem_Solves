i=lambda:map(int,input().split())
d1, d2, d3 =i()

min1=min(d1+d2+d3, 2*(d1+d2))
min2=min(2*(d1+d3), 2*(d2+d3))

print(min(min1, min2))
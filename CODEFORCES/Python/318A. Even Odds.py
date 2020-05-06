import math

inp=lambda:map(int,input().split())
n,k=inp()

div = math.ceil(n/2)
# print(div)
if k<=div:
    print(2*k - 1)
else:
    print(2 * (k-div))
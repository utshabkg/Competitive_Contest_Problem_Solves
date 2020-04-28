from math import gcd
A = int(input())
s = 0
for i in range(2, A):
    x = A
    while x!=0:
        s += x%i
        x = x//i
g = gcd(s, A-2)       
print(str(s//g)+"/"+str((A-2)//g))
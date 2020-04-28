import math

inp=lambda:map(int,input().split())

t = int(input())

for i in range(1,t+1):
    Ox,Oy, Ax,Ay, Bx,By = inp()

    d = math.sqrt((Ax-Bx)**2 + (Ay-By)**2)
    r = math.sqrt((Ax-Ox)**2 + (Ay-Oy)**2)
    theta = math.acos(1 - d**2/(2*r**2))

    print("Case %d" %i,":",r*theta)
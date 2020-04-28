
t = int(input())

for i in range(t):
    #n,a,b,c,d=inp()
    a = input().split(' ')
    
    s1 = int(a[1])-int(a[2]); e1 = int(a[1])+int(a[2])
    s2 = int(a[3])-int(a[4]); e2 = int(a[3])+int(a[4])
    
    if s2 > e1*int(a[0]) or e2 < s1*int(a[0]):
        print("NO")
    else:
        print("YES")

    # if (int(a[0]) * s1, int(a[0]) * e1) in range (s2,e2+1):# or (int(a[0]) * e1) in range (s2,e2+1):
    #     print("YES")
    # else:
    #     print("NO")
t = int(input())
for i in range(t):
    a = int(input())

    even = [2]
    odd = [1]

    if a==2 or a%2!=0 or (a//2)%2!=0:
        print("NO")

    else:
        for j in range(0,a//2-1):
            even.append(even[j]+2)
            
        for j in range(0, a//4):
            odd.append(even[j]-1)
            
        for j in range(a//4, a//2):
            odd.append(even[j]+1)
            
        print("YES")
        print(*sorted(set(even)), *sorted(set(odd)))

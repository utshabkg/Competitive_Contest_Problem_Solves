for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    
    sr = set(l)
    print(len(sr))

for _ in range(inin()):
    c = 0; flag = 1; l = []; t = ''
    n = inin()
    for i in range(n):
        s = stin()
        t += s
        # print(set(s))
        c += len(s)
        l += list(s)
        l = list(set(l))
        # print(l)
    # print(l)

    for i in range(len(l)):
        if t.count(l[i]) % n!=0:
            flag = 0
            break
    if c%n!=0:
        flag = 0

    if flag==1:
        print("Yes")
    else:
        print("No")
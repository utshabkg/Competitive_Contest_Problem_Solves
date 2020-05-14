inp=lambda:map(int,input().split())
t = int(input())

for _ in range(t):
    # import time
    # start_time = time.time()
    n = int(input())

    count = 0
    remain = 0
    i, j = 1, 1

    while i<n:
        if i==1:
            count += pow(2, i+2) * j
            j +=1

            i+=2
            # count += remain * j
            # count += pow(2, i+3) * (j+1) + pow(2, i+4) * (j+2)
        if i<n:
            remain = pow(i+2, 2) - pow(i, 2)
            count += remain * j
            j += 1

            if i==n-2:
                break
            remain = pow(i+4, 2) - pow(i+2, 2)
            count += remain * j
            j += 1

            if i==n-4:
                break
            remain = pow(i+6, 2) - pow(i+4, 2)
            count += remain * j
            j += 1

            if i==n-6:
                break
            remain = pow(i+8, 2) - pow(i+6, 2)
            count += remain * j
            j += 1

            if i==n-8:
                break
            remain = pow(i+10, 2) - pow(i+8, 2)
            count += remain * j
            j += 1

            i+=10
    print(count)
    # print("--- %s seconds ---" % (time.time() - start_time))
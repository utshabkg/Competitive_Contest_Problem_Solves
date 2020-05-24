mod = 10**6+3
ans = 1
inp=lambda:map(int,input().split())
t = int(input())
arr=[0]*(mod+1)
for i in range(1, mod+1):
    ans = ((i%mod)*(ans%mod))%mod #stored factorial upto each no in array
    arr[i] = ans
for _ in range(t):
    n, x = inp()

    if n>=mod:
# if no. is greater than mod that at sometome n! comes to mod also
# and n(1000003)% mod(which is also 1000003 ) gets 0 and hence 0
        print(0)
    else:
        ans = ((arr[n] % mod) * (x % mod)) %mod
        print(ans)

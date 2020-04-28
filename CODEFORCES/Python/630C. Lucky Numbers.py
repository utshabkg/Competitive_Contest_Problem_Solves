n = int(input())
count = 0

for i in range(1, n+1):
    count = count + 2**i

print(count)
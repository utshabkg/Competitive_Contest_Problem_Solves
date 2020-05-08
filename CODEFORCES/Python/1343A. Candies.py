t = int(input())

for i in range(t):
    n = int(input())
    temp = 3
	while n%temp > 0:
	    temp = temp*2 + 1

	print(n//temp)
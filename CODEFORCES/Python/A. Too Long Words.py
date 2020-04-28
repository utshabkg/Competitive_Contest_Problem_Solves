x = int(input())
for i in range(x):
 
	s = input()
	l = list(s)
	if(len(s) > 10):
		print(l[0] + str(len(l) - 2) + l[-1])
	else:
		print(s)

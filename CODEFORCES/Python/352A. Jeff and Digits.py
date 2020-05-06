n = int(input())
cnt = input().count('5')
if n == cnt:
	print('-1')
elif cnt < 9:
	print('0')
else:
	print('5' * (cnt // 9 * 9) + '0' * (n - cnt))
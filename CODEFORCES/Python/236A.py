s = input()
sr = sorted(s)
count = 0

for i in range(len(s)):
    if i>0 and sr[i-1]!=sr[i]:
        count = count+1

count = count+1
if count % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

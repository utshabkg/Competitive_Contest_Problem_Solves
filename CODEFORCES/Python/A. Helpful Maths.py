s = input()
sr = sorted(s)
last = []
for i in range(len(sr)):
    if sr[i]!='+':
        last.append(sr[i])
        last.append('+')

if last[-1]=='+':
    last.pop()

print(''.join(last))

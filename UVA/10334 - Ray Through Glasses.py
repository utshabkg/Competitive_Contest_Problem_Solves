#Uses Fibonacci

a,b = 0,1
table = []
for _ in range(1000):
    table.append(b)
    a,b = b, a+b

del table[1]

while(0 or 1):
    
    try:
        num = int(input())
        print(table[num])
    except Exception:
        break

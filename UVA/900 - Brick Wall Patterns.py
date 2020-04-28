#Uses Fibonacci

table = []
a,b = 0,1

for _ in range(50):
    table.append(b)
    a,b = b, a+b
 
while(0 or 1):
    
    try:
        num = int(input())
        if num == 0:
            break
        else:
            print(table[num])
    except EOFError:
        break

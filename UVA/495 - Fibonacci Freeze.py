# TLE
# def Fibonacci(x): 
#     if x<0: 
#         print("Incorrect input") 
#     # First Fibonacci number is 0 
#     elif x==1: 
#         return 0
#     # Second Fibonacci number is 1 
#     elif x==2: 
#         return 1
#     else: 
#         return Fibonacci(x-1)+Fibonacci(x-2) 

# while True:
#     n=int(input())
    
#     print("The Fibonacci number for",n,"is",Fibonacci(n+1))
#     if n==0:
#         break

table = []
a,b = 0,1

for _ in range(5000):
    table.append(b)
    a,b = b, a+b
 
while(0 or 1):
    
    try:
        num = int(input())
        if num == 0:
            print('The Fibonacci number for 0 is 0')
        else:
            print('The Fibonacci number for %d is'%num,table[num-1])
    except Exception:#EOFError:
        break

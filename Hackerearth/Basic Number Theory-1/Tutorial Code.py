'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

inp=lambda:map(int,input().split())

a, b, c, m = inp()

p, ans = 0, 0

def binaryExponentiation(b, n, m):
    if(n==0):
        return 1
    elif n%2 == 0:     #n is even
        return binaryExponentiation((b*b)%m,n//2, m)
    else:             #n is odd
        return (b*binaryExponentiation((b*b)%m,(n-1)//2, m))%m

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 

p = binaryExponentiation(a, b, m)
ans = ((p%m) * modInverse(c, m))%m
print(int(ans))
from sys import stdin,stdout

def love(i):
    if(i<9):
        return i;
    else:
        return i%9 + 10*love(i//9)
    
for n in stdin:
    n = int(n.rstrip('\n'))
    print(love(n))
for i in range(1, int(input())+1):
    s = input()

    if(s==s[::-1]):
        print('Case %d: Yes'%i)
    else:
        print('Case %d: No'%i)
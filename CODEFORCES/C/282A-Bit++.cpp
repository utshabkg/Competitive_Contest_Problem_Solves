#include<bits/stdc++.h>
int main()
{
    int n,x=0;
    char s[4];
    scanf("%d",&n);
    while(n--)
    {
        scanf("%s",s);

        if(s[1]=='+')
            x++;
        else
            x--;
    }

    printf("%d",x);
    return 0;
}

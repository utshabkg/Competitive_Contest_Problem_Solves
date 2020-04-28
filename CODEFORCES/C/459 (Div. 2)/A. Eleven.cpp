#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,j=0,x=0,y=1;
    scanf("%lld",&n);
    char s[1001];
    for(long long i=1;i<=n;i++)
    {
        if(x<=n&&y<=n)
        {
            j=x+y;
            x=y;
            y=j;
        }

        if(s[i]!='O')
            s[i]='o';
        if(j<=n)
            s[j]='O';
    }
    for(long long i=1;i<=n;i++)
        printf("%c",s[i]);

}

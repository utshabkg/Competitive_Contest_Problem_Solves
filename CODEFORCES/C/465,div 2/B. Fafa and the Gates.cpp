#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,i,x=0,y=0,p,q,cnt=0;
    scanf("%lld",&n);
    char s[n+1];
    scanf("%s",s);
    for(i=0;i<n;i++)
    {
        if(s[i]=='U')
            y++;
        else if(s[i]=='R')
            x++;
        if(x==y)
        {
            p=x,q=y;
            if(s[i]==s[i+1]&&s[i+1]=='U')
            {
                q++;
                if(y<q)
                    cnt++;
            }
            else if(s[i]==s[i+1]&&s[i+1]=='R')
            {
                p++;
                if(x<p)
                    cnt++;
            }
        }
    }
    printf("%lld\n",cnt);
}

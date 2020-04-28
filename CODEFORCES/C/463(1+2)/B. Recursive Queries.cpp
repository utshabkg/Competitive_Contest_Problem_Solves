#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n,l,r,k,i,j,a,b,c=0,cnt=0;
    scanf("%lld",&n);
    while(n--)
    {
        scanf("%lld%lld%lld",&l,&r,&k);
        for(i=l;i<=r;i++)
        {
            a=l/10;
            b=l%10;
            c=a*b;
            if(c==k)
                cnt++;
        }
        printf("%lld",cnt);
    }
}

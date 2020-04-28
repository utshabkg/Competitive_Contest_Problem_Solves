#include<bits/stdc++.h>
int main()
{
    long long n,a,b,c,cnt=0,i;
    scanf("%lld",&n);
    while(n--)
    {
        scanf("%lld %lld %lld",&a,&b,&c);
        if(a+b+c>=2)
            cnt++;
    }
    printf("%lld",cnt);
}

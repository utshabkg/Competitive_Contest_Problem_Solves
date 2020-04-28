#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,a,s1=0,s2=0;
    scanf("%lld",&n);
    while(n--)
    {
        scanf("%lld",&a);
        if(a>=0)
            s1=s1+a;
        else
            s2=s2+a;
    }
    printf("%lld\n",s1-s2);

}

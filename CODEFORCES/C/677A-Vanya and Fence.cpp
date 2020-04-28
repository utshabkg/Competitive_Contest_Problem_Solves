#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long a,n,h,i,cnt=0;
    cin>>n>>h;
    while(n--)
    {
        scanf("%lld",&a);
        if(a<=h)
            cnt++;
        else
            cnt+=2;
    }
    printf("%lld\n",cnt);
}

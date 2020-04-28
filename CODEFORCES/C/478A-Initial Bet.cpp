#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long a,b,c,d,e,x;
    scanf("%lld %lld %lld %lld %lld",&a,&b,&c,&d,&e);

    if(a>=0&&b>=0&&c>=0&&d>=0&&e>=0)
    {
        x=(a+b+c+d+e)/5;

        if((a+b+c+d+e)%5==0&&(a+b+c+d+e)!=0)
            cout<<x<<endl;
        else
            cout<<"-1\n";
    }
    else
        cout<<"-1\n";
}

#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,i;
    scanf("%lld",&n);

    for(i=1;i<=n;i++)
    {
        if(i%2!=0&&i==n)
            cout<<"I hate ";
        else if(i%2!=0&&i!=n)
            cout<<"I hate that ";
        else if(i%2==0&&i==n)
            cout<<"I love ";
        else if(i%2==0&&i!=n)
            cout<<"I love that ";
    }
    cout<<"it"<<endl;
}

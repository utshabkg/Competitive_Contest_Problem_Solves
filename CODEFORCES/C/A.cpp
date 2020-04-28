#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long l,r,a,s;
    cin>>l>>r>>a;
    if((l==0&&a==0)||(r==0&&a==0))
        s=0;

    else
    {
        if((s=l+r+a)%2==0)
            s=l+r+a;
        else
            s=l+r+a-1;
    }

    cout<<s;
}

#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,i,cnt=0;
    cin>>n;
    for(i=1;i<n;i++)
    {
        if(n%i==0)
            cnt++;
    }
    cout<<cnt<<endl;
}

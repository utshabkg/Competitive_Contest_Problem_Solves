#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,i,j;

    scanf("%d",&n);
    string s[n+1],t[n+1];
    for(i=1;i<=n;i++)
        cin>>s[i];

    for(i=1;i<=n;i++)
        for(j=1;i!=j,j<=n;j++)
    {
        t==strcat(s[i],s[j]);
        if(s[i]==t)
            printf("%d",i);
    }

}

#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,i,j,k;
    cin>>n;
    char s[n+1];
    for(i=0;i<=n;i++)
        scanf("%c",&s[i]);
    for(i=0;i<n;i++)
    {
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='y')
        {
            if(s[i+1]=='a'||s[i+1]=='e'||s[i+1]=='i'||s[i+1]=='o'||s[i+1]=='u'||s[i+1]=='y')
                {
                    s[i+1]='\0';
                }
        }

        for(j=0,k=0;k<n;k++)
            if(s[k]!='\0')
            {
                s[j]=s[k];
                j++;
            }
    }
    for(i=0;i<=n;i++)
        if(s[i]!='\0')
            printf("%c",s[i]);
}

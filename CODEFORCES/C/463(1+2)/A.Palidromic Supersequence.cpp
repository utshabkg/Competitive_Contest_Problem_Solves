#include<bits/stdc++.h>
using namespace std;
int main()
{
    char a[1010];
    scanf("%s",a);

    cout<<a;

    for(long long i=strlen(a)-1; i>=0; i--)
    {
            printf("%c",a[i]);
    }
}

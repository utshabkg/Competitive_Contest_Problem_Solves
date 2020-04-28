#include<bits/stdc++.h>
using namespace std;

int main()
{
    char S[101],P[27],Q[27];
    scanf("%s %s",S,P);
    int i,x;

    for(i=0;i<strlen(S);i++)
    {
        x=S[i]-97;
        Q[i]=P[x];
    }

    puts(Q);
}

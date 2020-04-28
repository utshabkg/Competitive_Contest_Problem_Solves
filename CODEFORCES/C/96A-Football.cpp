#include<bits/stdc++.h>
int main()
{
    char a,sx[100];
    scanf("%s",sx);
    int i,k=0,p=0;
    for(i=0,a=sx[0];strlen(sx)>i;i++)
    {
        if(a!=sx[i])
            p=1;
        else
            p++;
        if(p==7)
            break;

        a=sx[i];
    }

    if(p==7)
        printf("YES\n");
    else
        printf("NO\n");
}

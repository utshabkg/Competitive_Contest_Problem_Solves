#include<bits/stdc++.h>
int main()
{
    int n,i,a;
    char sx[100];
    scanf("%d",&n);
    for(i=1;n>=i;i++)
    {
        scanf("%s",sx);
        int a=(int)strlen(sx);
        if(a>10)
            printf("%c%d%c\n",sx[0],a-2,sx[a-1]);
        else
            printf("%s\n",sx);
    }
}

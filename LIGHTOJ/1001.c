#include<stdio.h>
#include<stdlib.h>

int main()
{
    int T,n,i;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d",&n);
        if(n>10)
            printf("%d %d\n",n-10,10);
        else
            printf("%d %d\n",n-n,n);
    }
}

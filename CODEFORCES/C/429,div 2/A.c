#include<stdio.h>
#include<stdlib.h>
#include<string.h
#include<math.h>

int main()
{
    int n,k,i;
    scanf("%d %d",&n,&k);
    char sx[n];
    for(i=0;i<n;i++)
    {
        scanf("%s",sx[i]);
    }

    for(i=0;i<n;i++)
    {
        if(sx[i]==sx[0])
            count++;
    }
}

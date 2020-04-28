#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int main()
{
    int N,K,count=0,num=0;
    scanf("%d %d",&N,&K);
    int ax[N],i,j;
    for(i=0;i<N;i++)
        scanf("%d",&ax[i]);
    for(i=0;i<N;i++){
        for(j=i+1;j<N;j++)
    {
        if(ax[i]==ax[j]&&ax[i]!=ax[i-1])
            count++;
        else
            continue;
        if(K<=count+1)
    {
        num++;
        break;
    }
    }
    }
    printf("%d\n",num);
}


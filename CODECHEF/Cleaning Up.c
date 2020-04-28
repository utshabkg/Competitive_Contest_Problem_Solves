#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int T,n,m,i,k,flag;
    scanf("%d",&T);
    while(T--)
    {
        int ax[1005]={0};
        scanf("%d %d",&n,&m);
        for(i=0;i<m;i++)
        {
            scanf("%d",&k);
            ax[k]=1;
        }
        flag=1;
        for(i=1;i<=n;i++)
        {
            if(ax[i]==0)
            {
                if(flag==1)
                {
                    printf("%d ",i);
                    flag=0;
                    ax[i]=1;
                }
                else
                    flag=1;
            }
        }
        printf("\n");
        for(i=1;i<=n;i++)
        {
            if(ax[i]==0)
                printf("%d ",i);
        }
        printf("\n");
    }
    return 0;
}

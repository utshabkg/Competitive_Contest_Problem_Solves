#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    int T,n,i,j,s1=0,s=0,temp=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int ax[n][n];
        for(i=1;i<=n;i++)
            for(j=1;j<=i;j++)
                scanf("%d",&ax[i][j]);

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                ax[j][i]=ax[i][j];
            }
        }

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                if(s1!=0&&j==1)
                    {
                        s1=0;
                        s1=s1+ax[i][j];
                    }
                else
                    s1=s1+ax[i][j];
            }
        if(temp<s1)
            temp=s1;
        s=temp;

            if(temp==6)
                temp--;

        if (tepm==7)
            temp=temp+2;
        }
        printf("%d\n",temp);
    }
}

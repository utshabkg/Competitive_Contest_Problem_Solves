#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    long long n,i,j,d,e,T;
    scanf("%lld",&T);
    while(T--)
    {
        scanf("%lld",&n);
        long long ax[n];
        for(i=0;i<n;i++)
            scanf("%lld",&ax[i]);
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
        {
            if(j==1)
                e=0;
            d=abs(ax[i]-ax[j]);

            if(d>=e&&j==1)
                e=d;
            else if(d<e)
                e=d;
        }
        printf("%lld\n",e);
    }
}

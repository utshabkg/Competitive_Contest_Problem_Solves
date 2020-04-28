#include<stdio.h>
int main()
{
    int n,k,i,sum=0,count=0,r=0;
    scanf("%d %d",&n,&k);
    int a[n];
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);

    for(i=0;i<n;i++)
    {
        sum=sum+a[i]+r;
        if(sum>8)
        {
            r=sum-8;
            count++;
        }
        else
        {
            count++;
            sum=0;
        }
    }
    if(k>8*n)
    printf("-1");
    else
    printf("%d",count);
}

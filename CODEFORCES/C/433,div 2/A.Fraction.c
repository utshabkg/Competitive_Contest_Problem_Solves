#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main()
{
    int sum,a,b,i,j;
    scanf("%d",&sum);
    if(sum%2!=0)
    {
        a=sum/2;b=sum/2+1;
    }
    else
    {
        if((sum/2)%2==0)
        {
            a=sum/2-1;b=sum/2+1;
        }
        else
        {
            a=sum/2-2;b=sum/2+2;
        }
    }
    printf("%d %d",a,b);
}

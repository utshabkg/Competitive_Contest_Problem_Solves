#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main()
{
    long long sum,A,B,a,b,s=0;
    scanf("%lld",&sum);
    if((sum/2)%2!=0)
    {
        A=sum/2-1;
        B=sum/2+1;
        printf("%lld %lld",A,B);
    }
    else if((sum/2)%2==0)
    {
        for(a=sum/2-1,b=sum/2+1;b>a;a/2,b/2)
        {
            if(b-a==1&&a+b==sum)
                break;
            else
            {
                a=a/2;
                b=b/2;
                s=a+b;
                if(s==sum)
                {
                    printf("%d %d",a,b);
                    break;
                }
            }
        }
    }

}

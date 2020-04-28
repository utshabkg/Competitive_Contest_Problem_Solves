#include<stdio.h>
int main()
{
    int A,i,j,d=0,q=0,s1=0,s2=1,count=0;
    scanf("%d",&A);

    for(i=2;i<A;i++)
    {
        for(j=i,d=A; ;)
        {
            d=d/i;
            q=d%i;
            s1=s1+q;
            if(d==0)
                break;
        }
        s2=s2+s1;
        count++;
    }
    printf("%d/%d",s2,count);
}

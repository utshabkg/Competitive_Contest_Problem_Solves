#include<stdio.h>
int main()
{
    long long n,m,a;
    long long x,y,total;
    scanf("%lld %lld %lld",&n,&m,&a);
    x=n/a;
    y=m/a;
    if(n%a!=0){x=x+1;}
    if(m%a!=0){y=y+1;}
    printf("%lld",x*y);
    return 0;
}

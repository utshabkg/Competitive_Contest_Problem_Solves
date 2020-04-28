#include<stdio.h>
int main()
{
    int M,N,x;
    scanf("%d %d",&M,&N);
    if((M*N)<=256)
        x=(M*N)/2;
    printf("%d",x);
}

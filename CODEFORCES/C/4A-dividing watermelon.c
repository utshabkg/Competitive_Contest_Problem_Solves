#include<stdio.h>
int main()
{
    int w;
    scanf("%d",&w);
    if(1<=w&&w<=100&&w!=2)
    {
        if(w%2==0)
            printf("YES");
        else
            printf("NO");
    }
    else
        printf("NO");
}

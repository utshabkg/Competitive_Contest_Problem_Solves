#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int A,B,S;
    scanf("%d %d",&A,&B);
    S=abs(A-B);
    if(S%10==9)
        printf("%d",--S);
    else
        printf("%d",++S);

}

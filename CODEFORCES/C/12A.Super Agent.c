#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main()
{
    char ax[3][3];
    int i,j;
    for(i=1;i<=3;i++){
        for(j=1;j<=3;j++)
    {
        scanf("%c",&ax[i][j]);
    }
    }
    if((ax[1][1]==ax[3][3])&&(ax[1][2]==ax[3][2])&&(ax[1][3]==ax[3][1])&&(ax[2][1]==ax[2][3]))
        printf("YES");
    else
        printf("NO");

}

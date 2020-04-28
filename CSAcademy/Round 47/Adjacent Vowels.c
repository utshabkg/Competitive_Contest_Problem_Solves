#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main()
{
    int N,i,count=0;

    scanf("%d",&N);
    char sx[N];
    scanf("%s",sx);

    for(i=0;i<strlen(sx);i++)
    {
        if((sx[i]=='a')||(sx[i]=='e')||(sx[i]=='i')||(sx[i]=='o')||(sx[i]=='u'))
        {
            if((sx[i+1]=='a')||(sx[i+1]=='e')||(sx[i+1]=='i')||(sx[i+1]=='o')||(sx[i+1]=='u'))
                count++;
        }
        else
            continue;
    }
    printf("%d",count);
}


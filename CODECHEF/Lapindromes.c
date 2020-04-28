#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

int main()
{
    int T,i,j,flag=0,x,y;
    char s;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s",s);
        if(strlen(s)%2==0)
        {
            for(i=0,j=strlen(s)-1;i<strlen(s)/2,j>=strlen(s)/2;i++,j--)
            {
                x=s[i];
                y=s[j];
                if(x==y)
                flag=1;
            }


        }
    }
}

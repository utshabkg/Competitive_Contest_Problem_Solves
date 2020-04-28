#include<bits/stdc++.h>
int main()
{
    char ax[110],bx[110];
    int i;
    scanf("%s %s",ax,bx);
    for(i=0;i<(strlen(ax));i++)
        {
            {
                if((tolower(ax[i])<tolower(bx[i]))||(tolower(ax[i])>tolower(bx[i])))
                    break;
            }
        }
            if(tolower(ax[i])<tolower(bx[i]))
                printf("-1");
            else if(tolower(ax[i])>tolower(bx[i]))
                printf("1");
            else if(tolower(ax[i])==tolower(bx[i]))
                printf("0");
}


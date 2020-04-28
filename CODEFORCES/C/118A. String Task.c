#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main()
{
    char sx[100],sy[100];
    int i,j=0;
    scanf("%s",sx);

    for(i=0;i<strlen(sx);i++)
    {

        if(sx[i]!='A'||sx[i]!='E'||sx[i]!='I'||sx[i]!='O'||sx[i]!='U'||sx[i]!='a'||sx[i]!='e'||sx[i]!='i'||sx[i]!='o'||sx[i]!='u')
            {sy[j]=sx[i];j++;}
    }

    printf(".%s",sy);
    return 0;
}

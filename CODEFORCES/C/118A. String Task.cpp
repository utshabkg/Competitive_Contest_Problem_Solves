#include<bits/stdc++.h>
main()
{
    char a[101];int i;
    gets(a);
    strlwr(a);
    for(i=0;a[i]!='\0';i++)
    {
        if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'||a[i]=='y')
            ;
        else
            printf(".%c",a[i]);}
}

/*int main()
{
    char c;
    while((c=getchar())!='\n'){
        c=tolower(c);
        if(c!='a' && c!='e'&&c!='i'&&c!='o'&&c!='u'&&c!='y'){
            printf(".%c",c);
        }
    }
}*/


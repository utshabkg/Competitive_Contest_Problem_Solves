#include<bits/stdc++.h>
using namespace std;

int main()
{
    double a,b;long long i;
    scanf("%lf %lf",&a,&b);



    a=a/1000000000000000000,b=b/1000000000000000000;
    for(i=0;;i++)
    {
        if(a==0&&b==0)
            break;
        else if(a>=2*b&&a!=0&&b!=0)
            a=a-2*b;
        else if(b>=2*a&&a!=0&&b!=0)
            b=b-2*a;
        else
            break;
    }
    printf("%lf %lf\n",a,b);
}

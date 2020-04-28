#include<bits/stdc++.h>
#include<math.h>

int main()
{
    int i, t, Ox,Oy, Ax,Ay, Bx,By;
    double d,r, theta;

    scanf("%d", &t);

    for(i=1;i<=t;i++)
    {
        scanf("%d %d %d %d %d %d", &Ox,&Oy, &Ax,&Ay, &Bx,&By);

        d = sqrt(pow(Ax-Bx, 2) + pow(Ay-By,2));
        r = sqrt(pow(Ox-Bx, 2) + pow(Oy-By,2));
        theta = acos(1 - pow(d,2)/(2*pow(r,2)));

        printf("Case %d: %lf\n", i, r*theta);

    }
}

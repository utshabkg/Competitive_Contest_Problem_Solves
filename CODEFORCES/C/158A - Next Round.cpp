#include<bits/stdc++.h>
int main()
{
    int n,k,i,cnt=0;
    scanf("%d %d",&n,&k);
    int a[n+1];

    for(i=1;i<=n;i++)
        scanf("%d",&a[i]);

    for(i=1;i<=n;i++)
        if(a[i]>=a[k]&&a[i]!=0)
            cnt++;

    printf("%d",cnt);

}

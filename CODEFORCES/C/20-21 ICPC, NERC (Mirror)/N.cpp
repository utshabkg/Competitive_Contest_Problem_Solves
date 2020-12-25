/// In the name of Allah SWT

using namespace std;
#include <bits/stdc++.h>

#define ll long long int
#define dd double

#define scl(x) scanf("%lld", &x)
#define scll(x, y) scanf("%lld %lld", &x, &y)
#define scd(x) scanf("%lf", &x)
#define scdd(x, y) scanf("%lf %lf", &x, &y)

#define prl(x) printf("%lld\n", x)
#define prll(x, y) printf("%lld %lld\n", x, y)
#define prYes printf("YES\n")
#define prNo printf("NO\n")
#define aNewLine printf("\n")

#define ON(n, i) (n | (1LL << i))
#define OFF(n, i) (n & (~(1LL << i)))
#define CHK(n, i) (n & (1LL << i))

#define For(i, x, y) for (ll i = x; i < y; i++)
#define Mem(ara, x) memset(ara, x, sizeof(ara))

#define pb push_back
#define pll pair<ll, ll>
#define ff first
#define ss second

#define maxn 200005LL ///2x10^5 + 5
//#define maxn 1000006LL ///10^6 + 6
//#define maxn 1000000009LL ///10^9 + 9

#define pi acos(-1.00)
#define eps 0.0000000001 ///10^-10
#define inf LONG_LONG_MAX
#define mod 1000000007LL ///10^9+7

ll t, test, temp;
ll n, m, k, kount;
ll a, b, c, ans, u, v;
ll x, y, z = -1, maxi, mini;
ll c1, c2, c3, a1, a2, a3, a4, a5;

void solve()
{
    cin >> c1 >> c2 >> c3;
    cin >> a1 >> a2 >> a3 >> a4 >> a5;

    if (a1 <= c1)
    {
        c1 -= a1;
    }
    else
    {
        prNo;
        return;
    }

    if (a2 <= c2)
    {
        c2 -= a2;
    }
    else
    {
        prNo;
        return;
    }

    if (a3 <= c3)
    {
        c3 -= a3;
    }
    else
    {
        prNo;
        return;
    }

    if (a4 <= c1 + c3)
    {
        if (a4 <= c1)
        {
            c1 -= a4;
        }
        else
        {
            c3 -= (a4 - c1);
            c1 = 0;
        }
    }
    else
    {
        prNo;
        return;
    }

    if (a5 <= c2 + c3)
    {
    }
    else
    {
        prNo;
        return;
    }

    prYes;
}

int main()
{
    test = 1;
    scl(test);
    while (test--)
        solve();
}

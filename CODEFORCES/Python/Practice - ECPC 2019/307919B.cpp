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

#define ON(n, i) (n|(1LL<<i))
#define OFF(n, i) (n&(~(1LL<<i)))
#define CHK(n, i) (n&(1LL<<i))

#define For(i, x, y) for(ll i = x; i < y; i++)
#define Mem(ara, x) memset(ara, x, sizeof(ara))

#define pb push_back
#define pll pair<ll, ll >
#define ff first
#define ss second

#define maxn 200005 ///2x10^5 + 5
//#define maxn 1000006 ///10^6 + 6
//#define maxn 1000000009 ///10^9 + 9

#define pi acos(-1.00)
#define eps 0.0000000001 ///10^-10
#define inf LONG_LONG_MAX
#define mod 1000000007 ///10^9+7

ll t, test, temp;
ll n, m, k, kount;
ll a, b, c, ans, u, v;
ll x, y, z = -1, maxi, mini;

double heron(double a, double b, double c)
{
    if (max({a, b, c}) * 2 > a + b + c)
        return 0;
    double s = (a + b + c) / 2.0;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}
double solve(double x, double y, double z)
{
    double ret = 0;
    double l = z, r = min(z + k, x + y);
    for (int i = 0; i < 100; ++i)
    {
        double per = (r - l) / 3.0;
        if (heron(x, y, l + per) > heron(x, y, r - per))
            r -= per;
        else
            l += per;
    }
    return heron(x, y, l);
}

dd ans2;

void solve2() {
    ll ara[3];
    cin >> ara[0] >> ara[1] >> ara[2] >> k;
    sort(ara, ara+3);
    ans2 = solve(ara[1], ara[2], ara[0]);
    cout << fixed << setprecision(11) << ans2 << endl;
}

int main() {
    #ifndef ONLINE_JUDGE

    #else
        freopen("sticks.in", "r", stdin);
    #endif

    test = 1;
    scl(test);
    while (test--) solve2();
}





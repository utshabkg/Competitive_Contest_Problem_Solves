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

void solve() {
    scl(n);
    ll init[n];
    ll speed[n];

    For (i, 0, n) scl(init[i]);
    For (i, 0, n) scl(speed[i]);

    /*
    k = 25;

    while (k--) {
        For (i, 0, n) {
            printf("%lld ", init[i]);
            init[i] += speed[i];
        }
        aNewLine;
    }
    */

    ll secondSpent = 0;

    For (i, 1, n) {

        init[i] += speed[i]*secondSpent;

//        printf("%lld -> ", i);
//        For (j, 0, n) {
//            printf(":%lld ", init[j]);
//        }
//        aNewLine;

        if (init[i-1] <= init[i]) {

        }
        else {

            ll toMovUp = init[i-1]-init[i];
            ll numerator = init[i-1] - init[i];
            ll denominator = speed[i] - speed[i-1];
            ll timeReq = numerator / denominator;

            if (timeReq < 0) {
                prl(z);
                return;
            }

            if (timeReq*denominator != numerator) {
                timeReq++;
            }

            init[i] += speed[i]*timeReq;
            secondSpent += timeReq;
        }

//        printf("%lld -> ", i);
//        For (j, 0, n) {
//            printf(":%lld ", init[j]);
//        }
//        aNewLine;
    }

    prl(secondSpent);
}

int main() {
    #ifndef ONLINE_JUDGE

    #else
        freopen("plants.in", "r", stdin);
    #endif

    test = 1;
    //scl(test);
    while (test--) solve();
}

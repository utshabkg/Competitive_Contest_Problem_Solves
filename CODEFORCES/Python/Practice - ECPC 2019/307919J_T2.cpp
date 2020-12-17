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

string str;

void solve() {

    cin >> n;
    cin >> str;

    ll bPosGiven = -1;
    ll aKount = 0, cKount = 0;

    bool aPresent = false, cPresent = false, bPresent = false;

    For (i, 0, n) {
        if (str[i] == 'b') {
            bPosGiven = i;
            bPresent = true;
        }
        else if (str[i] == 'a') {
            aKount++;
            aPresent = true;
        }
        else {
            cKount++;
            cPresent = true;
        }
    }

    if (bPresent and aPresent and (not cPresent)) {
        prl(z-z);
        return;
    }
    if (bPresent and cPresent and (not aPresent)) {
        prl(z-z);
        return;
    }
    if (aPresent and (not bPresent) and (not cPresent)) {
        prl(z-z);
        return;
    }
    if ((not aPresent) and (not bPresent) and cPresent) {
        prl(z-z);
        return;
    }
    if (bPosGiven == -1) {
        prl(z);
        return;
    }

    // abc
    string str1 = str;
    ll reqBPos = aKount;
    ll z1 = 0, z2 = 0;

    if (str1[reqBPos] != 'b') {
        swap(str1[bPosGiven], str1[reqBPos]);
        z1++;
    }
    for (ll i = 0; i < n; i++) {
        if (str1[i] == 'b') {
            break;
        }
        if (str1[i] != 'a') {
            z1++;
        }
    }

    //cba
    string str2 = str;
    reqBPos = cKount;
    if (str2[reqBPos] != 'b') {
        swap(str2[bPosGiven], str2[reqBPos]);
        z2++;
    }
    for (ll i = 0; i < n; i++) {
        if (str2[i] == 'b') {
            break;
        }
        if (str2[i] != 'c') {
            z2++;
        }
    }

    cout << min(z1, z2) << endl;


}

int main() {
    #ifndef ONLINE_JUDGE

    #else
        freopen("abc.in", "r", stdin);
    #endif

    test = 1;
    //scl(test);
    while (test--) solve();
}


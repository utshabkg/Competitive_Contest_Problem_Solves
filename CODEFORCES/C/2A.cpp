#include <bits/stdc++.h>

using namespace std;

// Input macros
#define si(n)                       scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9
#define MOD1                        1000000009
#define MOD2                        1000000007

// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd

// Useful container manipulation / traversal macros
#define FORI(i,n)                   for(i=0  ; i< n ;i++)
#define FORD(i,n)                   for(i=n-1; i>=0 ;i--)
#define FORall(i,a,b)               for(i=a  ; i<=b ;i++)
#define FOReach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair

// Some common useful functions
#define MAX(a,b)                     ( (a) > (b) ? (a) : (b))
#define MIN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

// datatypes
#define ll                           long long int
#define ull                          unsigned long long
#define ui                           unsigned int
#define us                           unsigned short
#define vi                           vector<int>
#define pii                          pair<int,int>
#define gc                           getchar
#define pc                           putchar

int main()
{
    map<string,int>score,test;
    map<string,int>::iterator it;
    string s[1001];
    int i,m=0,n,a[1001];
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>s[i]>>a[i];
        score[s[i]]+=a[i];
    }
    it=score.begin();
    while(it!=score.end())
    cout<<it->first<<" got "<<it->second<<endl;
}


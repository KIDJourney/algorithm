#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long LL;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const LL LLMax=((1LL<<62)-1+(1LL<<62));
const double eps=1e-9;
const double PI=atan(1.0)*4.0;

int k,vis[Maxn];
int sta[Maxn],dist[Maxn];
int bfs()
{
    int f=0,r=1;
    dist[f]=0;
    while(f!=r)
    {
        int &s=sta[f];
        if(s==k)
            return dist[f];
        if(s+1<=k&&vis[s+1]==0)
        {
            vis[s+1]=1;
            dist[r]=dist[f]+1;
            sta[r]=s+1;
            r++;
        }
        if(s-1>=0&&vis[s-1]==0)
        {
            vis[s-1]=1;
            dist[r]=dist[f]+1;
            sta[r]=s-1;
            r++;
        }
        if(abs(s*2-k)<=abs(s-k)&&vis[s*2]==0)
        {
            vis[s*2]=1;
            dist[r]=dist[f]+1;
            sta[r]=s*2;
            r++;
        }
        f++;
    }
    return -1;
}
int main(void)
{
// freopen("input.txt","r",stdin);
//	freopen("output","w",stdout);
    ios::sync_with_stdio(false);
    while(cin >> sta[0] >> k)
    {
        memset(vis,0,sizeof(vis));
        vis[sta[0]]=1;
        cout << bfs() << endl;
    }
    return 0;
}

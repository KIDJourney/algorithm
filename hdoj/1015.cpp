#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int target,in[20],ok,size;
char a[20],ans[5];
int f(char c,int x)
{
    int y=1,tp=c-'A'+1;
    for(int i=0; i<x; i++)
        y*=tp;
    return y;
}
bool judge()
{
    int temp=f(ans[0],1)-f(ans[1],2)+f(ans[2],3)-f(ans[3],4)+f(ans[4],5);
    if(temp==target)return true;
    return false;
}
bool cmp(char x,char y)
{
    return x>y;
}
void dfs(int n,int tot)
{
    if(tot==6)
    {
        if(judge())
            ok=1;
        return ;
    }
    if(n>=size)return;
    if(in[n])
    {
        dfs(n+1,tot);
        return;
    }
    ans[tot-1]=a[n];
    in[n]=1;
    dfs(0,tot+1);
    if(ok)return;
    in[n]=0;
    dfs(n+1,tot);
}
int main(void)
{
    while(~scanf("%d %s",&target,a),target)
    {
        size=strlen(a);
        sort(a,a+size,cmp);
        ok=0;
        ans[5]='\0';
        memset(in,0,sizeof(in));
        dfs(0,1);
        if(ok) printf("%s\n",ans);
        else puts("no solution");
    }
    return 0;
}

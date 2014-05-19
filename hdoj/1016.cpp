#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int ans[50];
int n;
int visit[50];
bool prime[50];
bool check(int step)
{
    if (step==0)
        return true;
    if (step==n-1)
        if (prime[ans[step]+ans[0]]&&prime[ans[step]+ans[step-1]])
            return true;
        else
            return false;
    if (prime[ans[step]+ans[step-1]])
        return true;
    return false;
}
void dfs(int num)
{
    if (num==n&&check(num-1))
    {
        for (int i=0;i<n-1;i++)
            printf("%d ",ans[i]);
        printf("%d\n",ans[n-1]);
        return ;
    }
    for (int i=1; i<=n; i++)
    {
        if (!visit[i])
        {
            ans[num]=i;
            if (check(num))
            {
                visit[i]=1;
                dfs(num+1);
                visit[i]=0;
            }
        }
    }
}


main()
{
    int t=1;
    memset(prime,1,sizeof(prime));
    for (int i=2;i<=40;i++)
    {
        if (prime[i])
        for (int j=2;i*j<40;j++)
        {
            prime[i*j]=0;
        }
    }

    while(~scanf("%d",&n))
    {
        printf("Case %d:\n",t++);
        ans[0]=1;
        memset(visit,0,sizeof(visit));
        visit[1]=1;
        dfs(1);
        printf("\n");
    }
}

//纯粹智商不够用，简单的dfs写了一个小时，水到爆了
//一开始脑子有问题用的字符数组存的，结果超过10就不能算了。
//啊啊啊啊啊啊我真的适合写代码么

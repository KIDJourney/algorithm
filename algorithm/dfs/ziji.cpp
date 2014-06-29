#include<iostream>
using namespace std;
int num[10]= {1,2,3,4,5};
int ans[10];
int dfs(int s,int now ,int all)
{
    if (now==all)
    {
        for (int i=0;i<now;i++)
            cout<<ans[i]<<' ';
        cout<<endl;
        return 1;
    }
    for (int i=s; i<5; i++)
    {
        ans[now]=num[i];
        dfs(i+1,now+1,all);
    }

main()
{
    for (int i=1; i<=5; i++)
    {
        dfs(0,0,i);
    }
}


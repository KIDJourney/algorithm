/*************************************************************************
	> File Name: 3278_2.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月02日 星期三 19时28分12秒
 ************************************************************************/

#include<iostream>
#include <climits>
#include<stdio.h>
#include<string.h>
using namespace std;
int s,e;
int visit[2000000];
int flag=0;
int abs(int a)
{
    if (a<0)
    return -a;
    else
    return a;
}
void dfs(int pos,int time,int all)
{
    if (pos==e)
    {
        flag=1;
        return;
    }
    if (time==all)
        return ;
    if (pos+1<=e&&!visit[pos+1])
    {
        visit[pos+1]=1;
        dfs(pos+1,time+1,all);
        visit[pos+1]=0;
    }
    if (pos-1>=0&&!visit[pos-1])
    {
        visit[pos-1]=1;
        dfs(pos-1,time+1,all);
        visit[pos-1]=0;
    }
    if (abs(pos*2-e)<=abs(e-pos)&&!visit[pos*2])
    {
        visit[pos*2]=1;
        dfs(pos*2,time+1,all);
        visit[pos*2]=0;
    }
}

main()
{
    while(~scanf("%d%d",&s,&e))
    {
        flag=0;
        memset(visit,0,sizeof(visit));
        for (int i=0; i<=INT_MAX; i++)
        {
            if (s>e)
            {
                printf("%d\n",s-e);
                break;
            }
            dfs(s,0,i);
            if(flag)
            {
                printf("%d\n",i);
                break;
            }
        }
    }
}

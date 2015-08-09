/*************************************************************************
	> File Name: 3278.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月03日 星期四 02时35分46秒
 ************************************************************************/
#include<string.h>
#include<stdio.h>
#include<iostream>
using namespace std;
int e,s;
int dist[200000];
int stac[200000];
int visit[200000];
int abs(int a)
{
    if (a>0)
    return a;
    else
    return -a;
}
int bfs()
{
    int f=0,r=1;
    dist[0]=0;
    while(f!=r)
    {
        int s = stac[f];
        if (s==e)
            return dist[f];
        if (s+1<=e&&!visit[s+1])
        {
            visit[s+1]=1;
            dist[r]=dist[f]+1;
            stac[r]=s+1;
            r++;
        }
        if (s-1>=0&&!visit[s-1])
        {
            visit[s-1]=1;
            dist[r]=dist[f]+1;
            stac[r]=s-1;
            r++;
        }
        if (abs(e-s*2)<abs(e-s)&&!visit[s*2])
        {
            visit[s*2]=1;
            dist[r]=dist[f]+1;
            stac[r]=s*2;
            r++;
        }
        f++;
    }
    return -1;
}
main()
{
    while(~scanf("%d%d",&s,&e))
    {
        memset(visit,0,sizeof(visit));
        stac[0]=s;
        visit[s]=1;
        cout<<bfs()<<endl;
    }
}


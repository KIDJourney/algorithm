#include<iostream>
#include<stdio.h>
using namespace std;

const int MAXN=60000;
int uset[MAXN];
int rank[MAXN]={1};
void mkset(int size)
{
    for (int i=0;i<size;i++)
        uset[i]=i;
    for (int i=0;i<size;i++)
        rank[i]=1;
    
}
int find(int x)
{
    if (x!=uset[x])
        uset[x]=find(uset[x]);
    return uset[x];
}
void unionset(int x,int y)
{
    if ((x=find(x))==(y=find(y)))  //赋值+判断是否属于同一集合
        return;
    else
        if (rank[x]>rank[y])
        uset[y]=x;
        else
    {
        uset[x]=y;
        if (rank[x]==rank[y])
            rank[y]++;
    }
}
main()
{
    int time=0;
    int ns,np;
    while(~scanf("%d%d",&ns,&np))
    {
        time++;
        if (!ns&&!np)
        break;
        int n1,n2;
        int ans=0;
        mkset(ns);
        for (int i=0;i<np;i++)
        {
            scanf("%d%d",&n1,&n2);
            unionset(n1,n2);
        }
        for(int i=0;i<ns;i++)
        {
            if (i==uset[i])
                ans++;
        }
        printf("Case %d: %d\n",time,ans);
    }
}

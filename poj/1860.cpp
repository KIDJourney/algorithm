/*************************************************************************
	> File Name: 1860.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月06日 星期日 11时05分06秒
 ************************************************************************/

#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<climits>
#include<cstring>
#include<string.h>
using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;

struct node
{
    int a;
    int b;
    double rate;
    double fee;
} exc[400];
double dis[400];
int n,m,s;
double v;
int all;

bool bellman()
{

    memset(dis,0,sizeof(dis));
    dis[s]=v;
    int flag=0;



    for (int i=1; i<=n-1; i++)
    {
        for (int j=0; j<all; j++)
            if (dis[exc[j].b]<(dis[exc[j].a]-exc[j].fee)*exc[j].rate)
                dis[exc[j].b]=(dis[exc[j].a]-exc[j].fee)*exc[j].rate;
    }



    for (int i=0;i<all;i++)
    {
        if (dis[exc[i].b]<(dis[exc[i].a]-exc[i].fee)*exc[i].rate)
            return true;
    }
    return false;
}
main()
{
    freopen("in.txt","r",stdin);
    while (cin>>n>>m>>s>>v)
    {

        all=0;
        for (int i=0; i<m; i++)
        {
            int a,b;
            double rab,cab,rba,cba;
            cin>>a>>b>>rab>>cab>>rba>>cba;
            exc[all].a=a;
            exc[all].b=b;
            exc[all].rate=rab;
            exc[all++].fee=cab;
            exc[all].a=b;
            exc[all].b=a;
            exc[all].rate=rba;
            exc[all++].fee=cba;
        }


        if (bellman())
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
}


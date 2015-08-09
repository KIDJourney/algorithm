/*************************************************************************
	> File Name: 1086_2.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月06日 星期日 10时55分25秒
 ************************************************************************/
#include<cstdio>
#include<iostream>
#include<string.h>
using namespace std;

int n;     //货币种数
int m;     //兑换点数量
int s;     //持有第s种货币
double v;  //持有的s货币的本金

int all;  //边总数
double dis[101];  //s到各点的权值

struct exchange_points
{
	int a;      //货币a
	int b;      //货币b
	double r;   //rate
	double c;   //手续费
}exc[202];

bool bellman(void)
{
	memset(dis,0,sizeof(dis));      //这里与bellman的目的刚好相反。初始化为源点到各点距离无穷小
	dis[s]=v;                       //即bellman本用于找负环，求最小路径，本题是利用同样的思想找正环，求最大路径

	/*relax*/

	bool flag;
	for(int i=1;i<=n-1;i++)
	{
		flag=false;
		for(int j=0;j<all;j++)
			if(dis[exc[j].b] < (dis[exc[j].a] - exc[j].c) * exc[j].r)         //寻找最长路径
			{                                                                 //进行比较的是"某点到自身的权值"和"某点到另一点的权值"
				dis[exc[j].b] = (dis[exc[j].a] - exc[j].c) * exc[j].r;
				flag=true;
			}
		if(!flag)
			break;
	}

	/*Search Positive Circle*/

	for(int k=0;k<all;k++)
		if(dis[exc[k].b] < (dis[exc[k].a] - exc[k].c) * exc[k].r)           //正环能够无限松弛
			return true;

	return false;
}

int main(void)
{
	int a,b;
	double rab,cab,rba,cba;   //临时变量
    freopen("in.txt","r",stdin);
	while(cin>>n>>m>>s>>v)
	{
		all=0;    //注意初始化
		for(int i=0;i<m;i++)
		{
			cin>>a>>b>>rab>>cab>>rba>>cba;
			exc[all].a=a;
			exc[all].b=b;
			exc[all].r=rab;
			exc[all++].c=cab;
			exc[all].a=b;
			exc[all].b=a;
			exc[all].r=rba;
			exc[all++].c=cba;
		}

	    /*Bellman-form Algorithm*/

	    if(bellman())
	    	cout<<"YES"<<endl;
	    else
	    	cout<<"NO"<<endl;
	}

	return 0;
}

/*************************************************************************
	> File Name: 2632.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月01日 星期二 11时51分19秒
 ************************************************************************/
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
struct robot
{
    int x,y;
    int dirct;
    robot(int tx,int ty,char dir)
    {
        x=tx,y=ty;
        if (dir=='N') dirct=0;
        if (dir=='E') dirct=1;
        if (dir=='S') dirct=2;
        if (dir=='W') dirct=3;
    }
    robot(){};
};
robot rob[200];
int map[200][200];
int d,w;
int n,o;
main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        memset(map,0,sizeof(map));
        int tx,ty;
        char td;
        scanf("%d%d",&w,&d);
        scanf("%d%d",&n,&o);
        for (int i=0;i<n;i++)
        {
            scanf("%d%d %c",&tx,&ty,&td);
            rob[i]=robot(tx,ty,td);
            map[tx][ty]=i;
        }
        for (int i=0;i<o;i++)
        {
            int nor,times;
            char order;
            scanf("%d %c%d",&nor,&order,&times);
        }
    }
}

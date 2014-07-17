/*************************************************************************
	> File Name: migong.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月04日 星期五 10时04分54秒
 ************************************************************************/

#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<climits>
#include<cstring>

using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;

int step;
int w,d;
int sx,sy;
char map[100][100];
int vis[100][100];
int flag=0;
int dir[4][2]={1,0,-1,0,0,1,0,-1};
int step_min=0;
int dfs(int x,int y,int now)
{
    step_min++;
    if (map[x][y]=='D')
        flag=1;
    if (flag)
        return 1;
    for (int i=0;i<4;i++)
    {
        int nx=x+dir[i][0];
        int ny=y+dir[i][1];
        if (!vis[nx][ny]&&map[nx][ny]!='X'&&nx>=0&&ny>=0&&nx<d&&ny<w)
        {
            vis[nx][ny]=1;
            dfs(nx,ny,now+1);
            if (flag)
            return 1;
            vis[nx][ny]=0;
        }
    }
}
main()
{
    freopen("in.txt","r",stdin);
    scanf("%d%d",&d,&w,&step);
    for (int i=0;i<d;i++)
        scanf("%s",map[i]);
    for (int i=0;i<d;i++)
        for (int j=0;j<w;j++)
    {
        if (map[i][j]=='S')
        {sx=i;sy=j;}
    }
    dfs(sx,sy,0);
    if (flag)
        cout<<"yes"<<step_min<<endl;
}

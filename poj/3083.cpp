/*************************************************************************
	> File Name: 3083.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月03日 星期四 17时44分56秒
 ************************************************************************/

#include<iostream>
#include<climits>
#include<cstring>
#include<cmath>
#include<cstdio>
using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;

int w,d;
int dir[4][2]= {-1,0,0,1,1,0,0,-1};
int ex,ey;
int step_lf,step_rf,step_min;
char map[300][300];

void dfs_lf(int x,int y,int face)
{
    step_lf++;
    if (x==ex&&y==ey)
        return;
    //int fd = (face-1+4)%4;
    for (int i=0; i<4; i++)
    {
    //    int  td = (fd+i)%4;
        int nx = x+dir[i][0];
        int ny = y+dir[i][1];
        if (map[nx][ny]!='#'&&nx>=0&&ny<=0&&nx<d&&ny<w)
            dfs_lf(nx,ny,i);
    }
}

main()
{
    freopen("in.txt","r",stdin);
    int sx,sy;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        step_lf=step_rf=step_min=0;
        int w,d;
        scanf("%d%d",&w,&d);
        for (int i=0; i<d; i++)
        {
            scanf("%s",map[i]);
            for (int j=0; j<w; j++)
                if (map[i][j]=='S')
                {
                    sx=i;
                    sy=j;
                }
                else if (map[i][j]=='E')
                {
                    ex=i;
                    ey=j;
                }
        }
        dfs_lf(sx,sy,0);
        cout<<step_lf;
    }
}


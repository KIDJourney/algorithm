/*************************************************************************
	> File Name: 2049.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月03日 星期四 16时26分46秒
 ************************************************************************/
#include <iostream>
#include <queue>
#include<string.h>
#include<cstdio>
using namespace std;
#define MAXV 210
#define INF 1<<29
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)

#define EMPTY 0
#define DOOR 1
#define WALL INF 

int xa[MAXV][MAXV],ya[MAXV][MAXV];
int dis[MAXV][MAXV];
int dt[4][2]={{-1,0},{0,1},{1,0},{0,-1}};
int xmax,ymax;

bool pd(int x,int y){
	if(x>0 && x<=xmax && y<=ymax && y>0) return 1;
	return 0;
}

int getvalue(int x,int y,int i){
	if(i==0) return ya[x-1][y];
	if(i==1) return ya[x][y];
	if(i==2) return xa[x][y-1];
	return xa[x][y];
}

int bfs(int tx,int ty){
	int i,j,vx,vy,dx,dy,tmp;
	queue <int>q;

	for(i=1;i<=ymax;i++){
		for(j=1;j<=xmax;j++)
			dis[i][j]=INF;
	}
	dis[1][1]=0;
	q.push(1);
	q.push(1);
	while(!q.empty()){
		vx=q.front();q.pop();
		vy=q.front();q.pop();

		for(i=0;i<4;i++){
			dx=vx+dt[i][0];
			dy=vy+dt[i][1];
			tmp=getvalue(vx,vy,i);
			if(pd(dx,dy) && dis[dx][dy]>dis[vx][vy]+tmp){
				dis[dx][dy]=dis[vx][vy]+tmp;
				q.push(dx);
				q.push(dy);
			}
		}
	}
	return (dis[tx][ty]==INF?-1:dis[tx][ty]);
}

int main(){
	int n,m,i,j;
	int x,y,d,t;
	double sx,sy;
	while(scanf("%d%d",&m,&n)){
		if(m==-1 && n==-1) break;

		ymax=xmax=-1;
		memset(xa,EMPTY,sizeof(xa));
		memset(ya,EMPTY,sizeof(ya));
		for(i=0;i<m;i++){
			scanf("%d%d%d%d",&x,&y,&d,&t);
			if(d){
				for(j=0;j<t;j++) ya[x][y+j+1]=WALL;
				ymax=max(y+t+1,ymax);
				xmax=max(x+1,xmax);
			}else{
				for(j=0;j<t;j++) xa[x+j+1][y]=WALL;
				ymax=max(y+1,ymax);
				xmax=max(x+t+1,xmax);
			}
		}

		for(i=0;i<n;i++){
			scanf("%d%d%d",&x,&y,&d);
			if(d) ya[x][y+1]=DOOR;
			else xa[x+1][y]=DOOR;
		}

		scanf("%lf%lf",&sx,&sy);
		if(!(sx>=1 && sx<=199 && sy>=1 && sy<=199)) printf("0\n");
		else printf("%d\n",bfs((int)sx+1,(int)sy+1));
	}
	return 0;
}

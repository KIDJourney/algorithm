#include<iostream>
#include<string.h>
#include<stdio.h>
#include<string>
using namespace std;
int mapsizex,mapsizey;
int map[100][100];
int dir[4][2]= {0,1,1,0,0,-1,-1,0};
int x,y;
int check(int x,int y)
{
    if(x<0||y<0||x>mapsizex||y>mapsizey)
        return false;
    return true;
}
int dti(char d)
{
    switch(d)
    {
    case 'N' :
        return 0;
    case 'E' :
        return 1;
    case 'S' :
        return 2;
    case 'W' :
        return 3;
    }
}
char itd(int i)
{
    switch(i)
    {
    case 0:
        return 'N';
    case 1:
        return 'E';
    case 2:
        return 'S';
    case 3:
        return 'W';
    }
}
main()
{
    ios::sync_with_stdio(false);
//    freopen("in.txt","r",stdin);
    int fd;
    char d;
    cin>>mapsizex>>mapsizey;
    string ord;
    memset(map,0,sizeof(map));
    int flag=0;
    while(cin>>x>>y>>d)
    {
        flag=0;
        cin>>ord;
        fd=dti(d);
        int len = ord.length();
        for (int i=0; i<len; i++)
        {
            int nx,ny;
            if (ord[i]=='R')
                fd=(fd+1)%4;
            if (ord[i]=='L')
                fd=(fd+3)%4;
            if (ord[i]=='F')
            {
                nx=x+dir[fd][0];
                ny=y+dir[fd][1];
                if(check (nx,ny))
                {
                    x=nx;
                    y=ny;
                }
                else
                {
                    if (map[x][y])
                    {
                        continue;
                    }
                    else
                    {
                        flag=1;
                        map[x][y]=1;
                    }
                    break;
                }
            }
        }
        cout<<x<<' '<<y<<' '<<itd(fd);
        if (flag)
            cout<<" LOST"<<endl;
        else
            cout<<endl;
    }
}

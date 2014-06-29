#include<iostream>
#include<stdio.h>
using namespace std;
const int MAXN=4;
bool flag=0;
bool map[MAXN][MAXN];
bool check()
{
    bool value = map[0][0];
    for (int i=0; i<MAXN; i++)
        for (int j=0; j<MAXN; j++)
        {
            if (value != map[i][j])
                return false;
        }
    return true;
}
void change(int x,int y)
{
    map[x][y]^=map[x][y];
    if (x>0)
        map[x-1][y]^=map[x-1][y];
    if (x<MAXN)
        map[x+1][y]^=map[x+1][y];
    if (y>0)
        map[x][y-1]^=map[x][y-1];
    if (y<MAXN)
        map[x][y+1]^=map[x][y+1];
}
int dfs(int x,int now ,int all)
{
    if (now==all)
    {
        flag = check();
        return 1 ;
    }
    for (int i=x; i<16; i++)
    {
        change(i/4,i%4);
        dfs(x+1,now+1,all);
        if (flag)
            return 1;
        change(i/4,i%4);
    }

}
main()
{
    ios::sync_with_stdio(false);
    int ans=0;
    char ch;
    for (int i=0; i<MAXN; i++)
        for (int j=0; j<MAXN; j++)
        {
            cin>>ch;
            if (ch=='b')
                map[i][j]=1;
            else
                map[i][j]=0;
        }
    for (int i=1; i<=16; i++)
    {
        flag=0;
        dfs(0,0,i);
        if (flag)
        {
            ans=i;
            break;
        }
    }
    if (flag)
        cout<<ans<<endl;
    else
        cout<<"Impossible"<<endl;
    return 0;
}


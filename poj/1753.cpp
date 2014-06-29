#include<iostream>
#include<stdio.h>
using namespace std;

const int MAXN = 4;
int MIN=1000;
int ans=0;
bool flag=0;
bool visit[MAXN][MAXN];
char input[MAXN][MAXN+1];
bool map[MAXN][MAXN];

void change(int x,int y)
{
    map[x][y]=!map[x][y];
    if (x>0)
        map[x-1][y]=!map[x-1][y];
    if (x<3)
        map[x+1][y]=!map[x+1][y];
    if (y>0)
        map[x][y-1]=!map[x][y-1];
    if (y<3)
        map[x][y+1]=!map[x][y+1];
}
bool check()
{
    bool value=map[0][0];
    for (int i=0; i<MAXN; i++)
        for (int j=0; j<MAXN; j++)
        {
            if (value!=map[i][j])
                return false;
        }
    return true;
}
void search(int m,int n)
{
    if(check())
    {
        flag=1;
        if (MIN>ans)
            MIN=ans;
        return;
    }
    if(m>=4)return;
    change(m,n);
    ans++;
    if(n<3)
        search(m,n+1);
    else
        search(m+1,0);
    change(m,n);
    ans--;
    if(n<3)
        search(m,n+1);
    else
        search(m+1,0);

}
int main()
{
    for (int i=0; i<MAXN; i++)
        scanf("%s",input[i]);
    for (int i=0; i<MAXN; i++)
        for(int j=0; j<MAXN; j++)
        {
            if (input[i][j]=='b')
                map[i][j]=1;
            else
                map[i][j]=0;
        }
    search(0,0);
    if (flag)
        printf("%d\n",MIN);
    else
        printf("Impossible\n");
    return 0;
}



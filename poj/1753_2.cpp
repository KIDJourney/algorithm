/*************************************************************************
	> File Name: 1753_2.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: 2014年06月29日 星期日 19时49分57秒
 ************************************************************************/

#include<iostream>
#include<stdio.h>
using namespace std;
bool flag=0;
bool map[4][4];
bool check()
{
    int value=map[0][0];
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
    {
        if (value != map[i][j])
            return false;
    }
    return true;
}
void change (int x,int y)
{
    map[x][y]=!map[x][y];
    if (x>0)
        map[x-1][y]= !map[x-1][y];
    if (x<3)
        map[x+1][y]= !map[x+1][y];
    if (y>0)
        map[x][y-1]= !map[x][y-1];
    if (y<3)
        map[x][y+1]= !map[x][y+1];

}
int dfs(int s,int now,int all)
{
    if (now ==all)
    {
        if (check())
            flag=1;
        return 1;
    }
    for (int i=s;i<16;i++)
    {
        change(i/4,i%4);
        dfs(i+1,now+1,all);
        change(i/4,i%4);
    }


}
main()
{
    char ch;
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
    {
        cin>>ch;
        if (ch=='b')
            map[i][j]=1;
        else
            map[i][j]=0;
    }
    int j;
    for (j=0;j<16;j++)
    {
        flag =0;
        dfs(0,0,j);
        if (flag)
        break;
    }
    if (flag)
        printf("%d\n",j);
    else
        printf("Impossible\n");
}
//好吧，个人还是比较讨厌这种dfs的，应该是题没刷够的原因碰到一点变化就蒙了。
//另一种方法是枚举所有情况然后找出最小数据。
//剪枝后发现可以直接从最小布数开始枚举。
//change函数一开始写错了，WA了半天。
//总体来说还是一道水题。

//果然自己太水了。。。。

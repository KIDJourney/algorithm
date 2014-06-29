#include<iostream>
#include<stdio.h>
using namespace std;
const int MAXN=4;
bool map[MAXN][MAXN];
main()
{
    ios::sync_with_stdio(false);
    char ch;
    for (int i=0;i<MAXN;i++)
        for (int j=0;j<MAXN;j++)
        {
            cin>>ch;
            if (ch=='+')
                map[i][j]=0;
            else
                map[i][j]=1;
        }
    for (int i=0;i<MAXN;i++){
        for (int j=0;j<MAXN;j++)
        {
            cout<<(map[i][j]?'-':'+');
        }
        cout<<endl;}
}


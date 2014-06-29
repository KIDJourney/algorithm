#include<iostream>
using namespace std;

const int MAXN=10;
int uset[MAXN];
int rank[MAXN]={1};
void mkset(int size)
{
    for (int i=0;i<size;i++)
        uset[i]=-1;
}
int find(int x)
{
    if (uset[x]<0)
    return x;
    if (x!=uset[x])
        uset[x]=find(uset[x]);
    return uset[x];
}
void unionset(int x,int y)
{
    if ((x=find(x))==(y=find(y)))
        return;
    if (uset[x]<uset[y])
    {
        uset[x]+=uset[y];
        uset[y]=x;
    }
    else
    {
        uset[y]+=uset[x];
        uset[x] = y;
    }
}

main()
{

}

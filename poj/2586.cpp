#include<iostream>
#include<stdio.h>
using namespace std;
int s,d;
bool num[12+3];
int Max=0;

inline bool check()
{
    int ans=0;
    for (int  i=0; i<8; i++)
    {
        ans=0;
        for (int  j=0; j<5; j++)
            ans+=num[i+j]?s:-d;
        if (ans>0)
            return false;
    }
    return true;
}
void doit(int  now)
{
    if (now == 12)
    {
        int ans=0;
        bool r=true;

        for (int  i=0; i<8; i++)
    {
        int ans2=0;
        for (int  j=0; j<5; j++)
            ans2+=num[i+j]?s:-d;
        if (ans2>0)
        {
        r=false;
            break;
            }
    }
    //return true;


        if (r)
        {
            for (int  i=0; i<12; i++)
                ans += num[i]?s:-d;
            if (ans>Max)
                Max=ans;
        }
        return ;
    }
    num[now]=1;
    doit(now+1);
    num[now]=0;
    doit(now+1);

}
int main()
{
    while(scanf("%d%d",&s,&d)!=EOF)
    {
        Max=0;
        doit(0);
        if (Max!=0)
            printf("%d\n",Max);
        else
            printf("Deficit\n");
    }
    return 0;
}

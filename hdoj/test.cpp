#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int n=8;
//int  ans[]="16743258";
int ans[8]={1,6,7,4,3,2,5,8};
bool prime[40];
bool check(int step)
{
    if (step==0)
        return true;
    if (step==n-1)
        if (prime[ans[step]+ans[0]]&&prime[ans[step]+ans[step-1]])
            return true;
        else
            return false;
    if (prime[ans[step]+ans[step-1]])
        return true;
    return false;
}
main()
{
    memset(prime,1,sizeof(prime));
    for (int i=2;i<=40;i++)
    {
        if (prime[i])
        for (int j=2;i*j<40;j++)
        {
            prime[i*j]=0;
        }
    }
    for (int i=0;i<40;i++)
    if(prime[i])
    cout<<i<<' ';
    cout<<endl;
    for (int i=0;i<8;i++)
        if (check(i))
           printf("Yes %d 's left is %d right is %d\n",ans[i],ans[i-1], ans[(i+1==n?0:i+1)]);
        else printf("No\n");
}


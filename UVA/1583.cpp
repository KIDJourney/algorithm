#include<iostream>
#include<stdio.h>
using namespace std;
int getnum(int n)
{
    int ans=0;
    while(n)
    {
        ans+=n%10;
        n/=10;
    }
    return ans;
}

main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int flag=0;
        int num;
        scanf("%d",&num);
        for (int i=num-54;i<=num;i++)
        {
            if(i<0)
                continue;
            if (i+getnum(i)==num)
                {flag=1;printf("%d\n",i);break;}
        }
        if (!flag)
            printf("0\n");
    }
}

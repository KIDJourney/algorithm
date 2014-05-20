#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
main()
{
    int ans[1000];
    int n,k;
    while(~scanf("%d %d",&n,&k))
    {
        int num=0;
        for (int i=0; i<n; i++)
            scanf("%d",&ans[i]);
        for (int i=0;i<k;i++)
            if (ans[i]>0)
                num++;
            else
                break;
        int pos=k;
        if (ans[k]>0)
            while(ans[pos]==ans[pos-1])
                pos++,num++;
        printf("%d\n",num);
    }
}


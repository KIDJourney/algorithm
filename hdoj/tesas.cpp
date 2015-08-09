#include<stdio.h>
#include<string.h>
#define MAX 50
int is_prime[MAX];
//int num[MAX];
void dfs(int n,int cur,int *num)
{
    if(cur==n&&!is_prime[num[0]+num[n-1]])
    {
        for(int i=0;i<n;i++)
        {
            if(i==0)
            printf("%d",num[i]);
            else
            printf(" %d",num[i]);
        }

        printf("\n");
    }
    else
    {
        for(int i=2;i<=n;i++)
        {
            num[cur]=i;
            int flag=1;
            for(int j=0;j<cur;j++)
            {
                if(num[j]==i)
                {
                    flag=0;
                    break;
                }
            }
            if(flag&&!is_prime[num[cur-1]+num[cur]])
            {
                dfs(n,cur+1,num);
            }
        }
    }
}

int main()
{
    memset(is_prime,0,sizeof(is_prime));
    int n;
    int cnt=0;
   // num[0]=1;
    is_prime[0]=1;
    is_prime[1]=1;
    for(int i=2;i<MAX;i++)
    {
        for(int j=i*i;j<MAX;j+=i)
        {
            is_prime[j]=1;
        }
    }
    while(scanf("%d",&n)>0)
    {
        int num[MAX];
        num[0]=1;
        cnt++;
        printf("Case %d:\n",cnt);
        dfs(n,1,num);
        printf("\n");
    }

}

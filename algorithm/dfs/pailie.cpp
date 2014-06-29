#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int len=0;
string word;
char ans[10000];
bool visit[10000];
void dfs(int n)
{
    if (n==len)
    {
        ans[len]='\0';
        cout<<ans<<endl;
        return;
    }
    for (int i=0;i<len;i++)
    {
        if (!visit[i])
        {
            ans[n]=word[i];
            visit[i]=1;
            dfs(n+1);
            visit[i]=0;
        }
    }
}
main()
{

   while(cin>>word)
    {
        memset(visit,0,sizeof(visit));
        len=word.length();
        dfs(0);

    }


}


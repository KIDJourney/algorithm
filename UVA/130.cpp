#include<iostream>
#include<queue>
#include<stdio.h>
using namespace std;
main()
{
    ios::sync_with_stdio(false);
    int n,k;
    queue<int> q;
    while(cin>>n>>k)
    {
        for (int i=1; i<=n; i++)
            q.push(i);
        while(q.size()!=1)
        {
            int len=q.size();
            int t = k %len;
            for (int i=0;i<k-1;i++)
            {
                q.push(q.front());
                q.pop();
            }
            q.pop();
        }
        cout<<q.front()<<endl;
        q.pop();
    }

}

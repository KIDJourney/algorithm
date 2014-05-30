#include<iostream>
#include<queue>
using namespace std;
int doit(int n)
{
    if (n==13)
        return 1;
    for (int ans=2; ans<n; ans++)
    {
        queue<int> line;
        for (int i=1; i<=n; i++)
            line.push(i);
        while(line.front()!=13&&line.size())
        {
            line.pop();
            for (int i=0; i<ans-1; i++)
            {
                line.push(line.front());
                line.pop();
            }
        }
        if (line.size()==1)
            return ans;
    }
}
main()
{
    ios::sync_with_stdio(false);
    int n;
    while(cin>>n)
    {
        if(!n)
        break;
        cout<<doit(n)<<endl;
    }
}

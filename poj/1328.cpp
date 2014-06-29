#include<iostream>
#include<algorithm>
using namespace std;
struct duan
{
    double left;
    double right;
};
bool cmp(duan a, duan b)
{
    return a.left<b.left;
}
main()
{
    int time=0;
    duan line[3000];
    ios::sync_with_stdio(false);
    int n,r;
    int flag=0;
    while(cin>>n>>r)
    {
        time++;
        int ans=1;
        flag =0;
        if (n==0&&r==0)
            break;
        int x,y;
        for (int i=0; i<n; i++)
        {
            cin>>x>>y;
            if (y>r)
                flag=1;
            line[i].left = x-sqrt(r*r-y*y);
            line[i].right=x+ sqrt(r*r-y*y);
        }
        sort(line,line+n,cmp);
        double right = line[0].right;
        for (int i=1; i<n; i++)
        {
            if (line[i].right <right)
                right=line[i].right;
            else if (line[i].left>right)
            {
                ans++;
                right = line[i].right;
            }
        }
        printf("Case %d: %d\n",time,flag?-1:ans);
    }
}

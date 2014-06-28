#include<iostream>
#include<stdio.h>
using namespace std;
struct point
{
    int x,y;
    point (int a,int b):x(a),y(b) {}
};
int check(int k,point s,point goal)
{
    int ans=0;
    if (!k)
        return 0;
    point left_top(s.x-k,s.y-k);
    point right_bottom(s.x+k,s.y+k);
    if (left_top.x<0||left_top.y<0)
        return 0;
    if (right_bottom.x>2048||right_bottom.y>2048)
        return 0;
    if( goal.x >= left_top.x && goal.x <= right_bottom.x )
        if( goal.y >= left_top.y &&goal.y <= right_bottom.y )
            ans++;
    ans+=check(k/2,left_top,goal);
    ans+=check(k/2,right_bottom,goal);
    ans+=check(k/2,point(left_top.x,right_bottom.y),goal);
    ans+=check(k/2,point(right_bottom.x,left_top.y),goal);
    return ans;
}
main()
{
    int k,x,y;
    while(cin>>k>>x>>y)
    {
        if (x==0&&y==0&&k==0)
            break;
        point map(1024,1024);
        cout<<check(k,map,point(x,y))<<endl;
    }
}


//图怎么建的。
//21那里为啥是大于。
//蛋碎了

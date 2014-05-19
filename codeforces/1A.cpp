#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
    ios::sync_with_stdio(false);
    long long n,m,a;
    while(cin>>n>>m>>a)
    {
        long long x=n/a;
        long long y=m/a;
        if (x*a<n)
            x++;
        if (y*a<m)
            y++;
        cout<<x*y<<endl;

    }

    return 0;
}


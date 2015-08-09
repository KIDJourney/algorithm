/*************************************************************************
	> File Name: 448D.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月18日 星期五 15时34分25秒
 ************************************************************************/

#include<bits/stdc++.h>

using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;

long long cul(long long n,long long m,long long x)
{
    long long sum=0;
    for (int i=1; i<=n; i++)
        sum+=min(m,(x-1)/i);
    return sum;
}

main()
{
    long long n,m,k;
    cin>>n>>m>>k;
    long long l = 1 , r = n*m+1;
    while (l<r)
    {
        long long  x = (l+r)/2;
        if (cul(n,m,x)<k)
            l = x+1;
        else
            r = x;
    }
    cout<<l-1<<endl;
}


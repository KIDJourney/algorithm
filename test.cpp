/*************************************************************************
	> File Name: test.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月04日 星期五 09时35分24秒
 ************************************************************************/

#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<climits>
#include<cstring>

using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;
main()
{
    char s;
    int w;
    int d;
    char temp;
    scanf("%d%d",&w,&d);
    for (int i=0;i<d;i++)
        for (int j=0;j<w;j++)
    {
        scanf("%c",&temp);
        printf("%c",temp);
    }
}

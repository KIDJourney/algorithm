//#include<iostream>
//#include<stdio.h>
//#include<math.h>
//using namespace std;
//long long n,p;
//long long halffind(long long s,long long e)
//{
//    long long mid=(s+e)/2+1;
//    long long ans=1;
//    for (int i=0;i<n;i++)
//    {
//        ans*=mid;
//        if (ans>p)
//            break;
//    }
//    if (ans==p)
//        return mid;
//    if (ans>p)
//        return halffind(s,mid);
//    else
//        return halffind(mid+1,e);
//}
//main()
//{
//    freopen("in.txt","r",stdin);
//    while(~scanf("%lld %lld",&n,&p))
//    {
//        if (n==2)
//            {printf("%.0lf\n",sqrt(p));continue;}
//        if (p==1)
//            {printf("0\n");continue;}
//        int mid=sqrt(p);
//        printf("%lld\n",halffind(0,mid));
//    }
//}
//妈蛋二分过不了大数据
#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
main()
{
    double n,p;
    while(~scanf("%lf %lf",&n,&p))
        printf("%.0lf\n",pow(p,1/n));
}

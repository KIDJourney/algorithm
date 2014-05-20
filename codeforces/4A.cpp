#include<stdio.h>
#include<iostream>
using namespace std;
main()
{
    int n;
    while(~scanf("%d",&n))
    {
    if (n%2==0&&n!=2)
            printf("YES\n");
        else
            printf("NO\n");
    }
}

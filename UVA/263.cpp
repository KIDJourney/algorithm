#include<iostream>
#include<string>
#include<stdio.h>
#include<algorithm>
#include<cstring>
using namespace std;
main()
{

    long long n1;
    while(scanf("%lld",&n1))
    {
        char num2[10];
        char num1[10];
        sprintf(num1,"%lld",n1);
        sprintf(num2,"%lld",n1);
        sort(num1,num1+strlen(num1), greater<char>());
        sort(num2,strlen(num2)+num2, less<char>());
        sscanf(num1,"%lld",n1);
        sscanf(num2,"%lld",n2);
        char ans1[10];
        char ans2[10];
        long long n2;
        sscanf()

    }
}


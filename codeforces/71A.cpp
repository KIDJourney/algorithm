#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
main()
{
    string temp;
    int n;
    scanf("%d",&n);
    while(n--)
    {
        cin>>temp;
        int len=temp.length();
        if (len>10)
            printf("%c%d%c\n",temp[0],len-2,temp[len-1]);
        else
            printf("%s\n",temp.c_str());

    }
}


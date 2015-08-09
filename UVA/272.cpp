#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
main()
{
    int flag=0;
    char word;
    while((word=getchar())!=EOF)
    {
        if (word=='"')
            if (!flag)
            {printf("``");flag=!flag;}
            else
            {printf("''");flag=!flag;}
        else
            printf("%c",word);
    }  
}

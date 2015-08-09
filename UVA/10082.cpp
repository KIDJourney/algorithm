#include<iostream>
#include<cstring>
using namespace std;
main()
{
    char line[]="1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    char word;
    while((word=getchar())!=EOF)
    {
        int flag=0;
        for (int i=0;i<word;i++)
        {
            if (word==line[i])
            {
                flag=1;
                printf("%c",line[i-1]);
                break;
            }
        }
        if (!flag)
            putchar(word);
    }
}

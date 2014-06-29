/*************************************************************************
	> File Name: test.cpp
	> Author: ma6174
	> Mail: ma6174@163.com
	> Created Time: 2014年06月29日 星期日 21时38分21秒
 ************************************************************************/

#include<iostream>
using namespace std;
main()
{
    for (int i=0;i<=(1<<6)-1;i++)
    {
        int num=i;
        cout<<num<<endl;
        for (int j=0;j<5;j++)
        {
            cout<< (num&1);
            num = num >>1;
        }
        cout<<endl;
    }
}

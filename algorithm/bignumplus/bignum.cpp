/*************************************************************************
	> File Name: bignum.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: 2014年06月29日 星期日 17时25分11秒
 ************************************************************************/

#include<iostream>
#include<string>
using namespace std;
struct bignum{
    int len;
    string num;
    bignum operator + (bignum a);
    void show()
    {
        for (int i=len-1;i>=0;i++)
        cout<<num[i];
        cout<<endl;
    }
};

bignum bignum:: operator + (bignum a)
{

    bignum ans;
    int uper=0;
    int lenght  = max(len,a.len);
    for (int i=0;i<lenght;i++)
    {
        int temp=uper + num[i]?(num[i]-'0'):0 + a.num[i]?(num[i]-'0'):0;
        uper = temp / 10;
        ans.num+= temp % 10 +'0';
    }
    return ans;
}
main()
{
    
}

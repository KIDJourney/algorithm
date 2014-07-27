/*************************************************************************
	> File Name: 1035.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月27日 星期日 10时28分17秒
 ************************************************************************/

#include<stdio.h>
#include<string>
#include<iostream>
#include<cmath>
using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;
int dabs(int a)
{
    if (a<0)
        a = -a;
    return a;
}
bool check(string a, string b )
{
    int lena = a.length();
    int lenb = b.length();
    if (lena==lenb)//change
    {
        int flag=0;
        int diff=0;
        for (int i=0;i<lena;i++)
        {
            if (a[i]!=b[i])
                diff++;
            if (diff>1)
            {
                flag=1;
                break;
            }
        }
        if (!flag)
            return true;
    }
    if (lena>lenb)//del 
    {
        int flag=0;
        int diff=0;
        int pa=0,pb=0;
        while (pa!=lena)
        {
            if (a[pa]!=b[pb])
            {
                diff++;
                pa++;
            }
            else
            {
                pa++;
                pb++;
            }
            if (diff>1)
            {
                flag=1;
                break;
            }
        }
        if (!flag)
            return true;
    }
    if (lena<lenb)//add
    {
        int flag=0;
        int pa=0,pb=0;
        int diff=0;
        while (pa!=lena)
        {
            if (a[pa]!=b[pb])
            {
                pb++;
                diff++;
            }
            else
            {
                pa++;
                pb++;
            }
            if (diff>1)
            {
                flag=1;
                break;
            }
        }
        if (!flag)
            return true;
    }
    return false;
}
int main()
{
    ios::sync_with_stdio(false);
    //freopen("in.txt","r",stdin);
    string dic[10005];
    int dnum=0;
    while (cin>>dic[dnum])
        if (dic[dnum++]=="#")
        {
            dnum--;
            break;
        }
    string word;
    while (cin>>word)
    {
        int flag=0;
        if (word=="#")
            break;
        for (int i=0;i<dnum;i++)
            if (word==dic[i])
        {
                cout<<word<<" is correct"<<endl;
                flag=1;
                break;

        }
        if (flag)
            continue;
        cout<<word<<':';
        for (int i=0;i<dnum;i++)
        {
            if (dabs(int(dic[i].length())-int(word.length()))<=1)
                if (check(dic[i],word))
                    cout<<' '<<dic[i];
        }
        cout<<endl;
    }
    return 0;
}

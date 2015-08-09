/*************************************************************************
	> File Name: teststring.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月27日 星期日 11时13分16秒
 ************************************************************************/

#include<bits/stdc++.h>

using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;
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


main()
{
    string a;
    string b;
    while (cin>>a>>b)
    {
        if (check(a,b))
            cout<<"yes"<<endl;
        else
            cout<<"no"<<endl;
    }
}

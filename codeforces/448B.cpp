/*************************************************************************
	> File Name: 448B.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月18日 星期五 14时54分16秒
 ************************************************************************/

#include<bits/stdc++.h>

using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-9;
const double PI=atan(1.0)*4.0;
main()
{
    int worda[26]= {};
    int wordb[26]= {};
    string a,b;
    cin>>a>>b;
    int lena = a.length();
    int lenb = b.length();
    for (int i=0; i<lena; i++)
        worda[a[i]-'a']++;
    for (int i=0; i<lenb; i++)
        wordb[b[i]-'a']++;
    int automaton=0;
    int array =0;
    int flag=0;
    for(int i=0; i<26; i++)
    {
        if (worda[i]<wordb[i])
        {
            cout<<"need tree"<<endl;
            flag=1;
            break;
        }
        if (worda[i]>wordb[i])
            automaton=1;
    }
    if (flag)
        return 0;
    int pos=0;
    for (int i=0; i<lenb; i++)
    {
        int flagn=0;
        for (int j=pos;j<lena; j++)
        {
            if (a[j]==b[i])
            {   
                pos=j+1;
                flagn=1;
                break;
            }
        }

        if (!flagn)
        {
            array=1;
            break;
        }
    }
    if (automaton && array)
        cout<<"both"<<endl;
    else if (array)
        cout<<"array"<<endl;
    else
        cout<<"automaton"<<endl;
}


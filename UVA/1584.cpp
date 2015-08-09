#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
bool cmp(string s1,string s2)  //s1>s2
{
    int len = s1.length();
    for (int i=0; i<len; i++)
    {
        if (s1[i]==s2[i])
            continue;
        if (s1[i]>s2[i])
            return true;
        else
            return false;
    }
}
main()
{
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    while(t--)
    {
        string word;
        cin>>word;
        int len = word.length();
        string pre=word;
        for (int i=0;i<len;i++)
        {
            string now;
            for (int j=i;j<len;j++)
                now +=word[j];
            for (int x= 0 ;x<i;x++)
                now+=word[x];
            if (cmp(pre,now))
                pre=now;
        }
        cout<<pre<<endl;
    }
}

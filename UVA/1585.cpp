#include<iostream>
#include<string>
using namespace std;
main()
{
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    while(t--)
    {
        int ans=0;
        string word;
        cin>>word;
        int value=0;
        int len = word.length();
        for (int i=0;i<len;i++)
        {
            if (word[i]=='O')
                {value++;ans+=value;}
            else
                value=0;
        }
        cout<<ans<<endl;
    }
}

/*************************************************************************
	> File Name: 1068.cpp
	> Author: ma6174
	> Mail: ma6174@163.com
	> Created Time: 2014年06月30日 星期一 23时04分10秒
 ************************************************************************/

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
        string symbol;
        int n;
        cin>>n;
        int temp;
        int pre=0;
        for (int i=0; i<n; i++)
        {
            cin>>temp;
            for (int j=0; j<temp-pre; j++)
                symbol+='(';
            symbol+=')';
            pre = temp;
        }
        int len =symbol.length();
        int flag=0;
        for (int i=0; i<len; i++)
        {
            if (symbol[i]==')')
            {
                int j=i;
                int ans=0;
                int nor=0,nol=0;
                while(j>=0)
                {
                    if (symbol[j]==')')
                        nor++;
                    else
                        nol++;
                    if (nor==nol&&nor!=0)
                    {
                        ans=nor;
                        break;
                    }
                    j--;
                }
                if (flag==0)
                    cout<<ans;
                else
                    cout<<' '<<ans;
                flag=1;
            }
        }
        cout<<endl;
    }

}

#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
main()
{
//    freopen("in.txt","r",stdin);
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        cin.ignore();
        string wu[300];
        string goal[300];
        for (int i=0;i<n;i++)
            getline(cin,wu[i]);
        for (int i=0;i<n;i++)
            getline(cin,goal[i]);

        int i,j;
        i=j=n-1;
        while(i>=0)
        {
            if (wu[i]==goal[j])
                i--,j--;
            else
                i--;
        }
        for (;j>=0;j--)
            cout<<goal[j]<<endl;
        cout<<endl;
    }
}

#include<iostream>
using namespace std;
main()
{
        int t;
        cin>>t;
        while(t--)
        {
            int x,y;
            cin>>x>>y;

            if ((x-2)%3!=0)
                x=(x-2)/3+1;
            else
                x=(x-2)/3;
            if ((y-2)%3!=0)
                y= (y-2)/3+1;
            else
                y=(y-2)/3;
            printf("%d\n",x*y);
        }
}



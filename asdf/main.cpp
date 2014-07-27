/*************************************************************************
	> File Name: 1_1010.cpp
	> Author: KIDJourney
	> Mail: kingdeadfishcn@gmail.com
	> Created Time: 2014年07月22日 星期二 13时00分09秒
 ************************************************************************/
#include <algorithm>
#include<bits/stdc++.h>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int Maxn=2e6+3;
const int MaxHashSize=(1<<16)+3;
const double eps=1e-5;
const double PI=atan(1.0)*4.0;
struct Account
{
    double rating;
    double possibility;
    Account()
    :rating(0.0),possibility(0.0)
    {

    }
};
int main()
{
    int temp;
    while(cin >> temp)
    {
        Account account1,account2;
        account1.possibility = temp;
        account2.possibility = temp;
        account1.rating = 0.0;
        account2.rating = 0.0;
        double count = 0;
        while(1000 - account1.rating >= eps ||
             1000 - account2.rating >= eps )
        {
            if(account1.rating <= account2.rating && 1000 - account1.rating >= eps)
            {
                account1.rating = min(account1.rating + 50, 1000.0) * temp
                                    + max(account1.rating - 1000,0.0) * (1.0 -  temp);
                     ++count;

            }
              else if(1000 - account1.rating < eps || 1000 - account2.rating < eps)
            {
                break;
            }

            else if(account1.rating > account2.rating && 1000 - account2.rating >= eps)
            {
               account2.rating = min(account2.rating + 50, 1000.0) * temp
                                    + max(account2.rating - 1000,0.0) * (1 -  temp);
                ++count;
            }
            else if(1000 - account1.rating < eps || 1000 - account2.rating < eps)
            {
                break;
            }


        }
        printf("%.6lf\n",count);
    }
    return 0;
}

#include<iostream>
using namespace std;
main()
{
    int n;
    cin>>n;
    int num;
    long long  ans = n*5;
    int pre = 0;
    for (int i = 0 ; i < n ; i++ ){
        cin>>num;
        if (num>pre){
            ans += (num-pre) * 6;
        } else {
            ans += (pre - num) * 4;
        }
        pre = num;
    }
    cout<<ans;

}

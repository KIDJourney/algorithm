#include<iostream>
using namespace std;
main()
{
    long long number[1005];
    int index;
    long long n , b;
    while(cin>>n>>b){
        while(n){
            number[index++] = n % b;
            n /= b;
        }
        int i = 0 ;
        int j = index - 1;
        int flag = 1;
        while(i<=j){
            if (number[i] != number[j]){
                flag = 0;
                break;
            }
            i++;
            j--;
        }
        if (flag){
            cout<<"Yes"<<endl;
        } else {
            cout<<"No"<<endl;
        }
        for(int i = index - 1 ; i >0 ; i--){
            cout<<number[i]<<' ';
        }
        cout<<number[0]<<endl;
    }
}

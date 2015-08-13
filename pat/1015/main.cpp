#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<string>
#include<math.h>

#define N 100005
using namespace std;
bool prime[N];
void IsPrime(){
     prime[0]=prime[1]=0;prime[2]=1;
     for(int i=3;i<N;i++)
        prime[i]=i%2==0?0:1;
     int t=(int)sqrt(N*1.0);
     for(int i=3;i<=t;i++)
       if(prime[i])
         for(int j=i*i;j<N;j+=2*i)
            prime[j]=0;
}
main()
{
    IsPrime();
    int n , d;
    while(cin>>n){
        if (n < 0){
            break;
        }
        if (n == 1){
            cout<<"No"<<endl;
            continue;
        }
        cin>>d;
        if (!prime[n]){
            cout<<"No"<<endl;
            continue;
        }
        string num;
        while(n){
            int left = n % d;
            n /= d;
            num += '0' + left;
        }
        int sum = 0;
        for(int i = 0 , len = num.length() ; i < len ; i++){
            sum *= d;
            sum += num[i] - '0';
        }
        if (prime[sum]){
            cout<<"Yes"<<endl;
        } else {
            cout<<"No"<<endl;
        }
    }
}

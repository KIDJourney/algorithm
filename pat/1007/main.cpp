#include<iostream>
using namespace std;
main()
{
    int number[10005];
    int s = 0 ;
    int e = 0 ;
    int start = 0;
    int tend = 0;
    int n;
    cin>>n;
    tend = n-1;
    int thissum = 0;
    int maxsum = 0;
    for (int i = 0 ; i < n ; i++){
        cin>>number[i];
    }
    for (int i = 0 ; i < n ; i++){
        if (thissum >= 0){
            thissum += number[i];
            e = i;
        } else {
            thissum = number[i];
            s = i;
            e = i;
        }
        if (thissum > maxsum || (thissum == 0 && tend == n-1)){
            maxsum = thissum;
            start = s;
            tend = e;
        }
    }
    cout<<maxsum<<' '<<number[start]<<' '<<number[tend];



}

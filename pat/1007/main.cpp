#include<iostream>
using namespace std;
main()
{
    int n;
    int maxsum = 0;
    int thissum = 0 ;
    int s = 0 ;
    int e = 0 ;
    int start ,  tend;
    int number[10005];
    cin>>n;
    for(int i = 0 ; i < n ; i++){
        cin>>number[i];
    }
    for(int i = 0 ; i < n ; i++){
        thissum += number[i];
        e = i ;
        if (thissum > maxsum){
            maxsum = thissum;
            start = s;
            tend = e;
        } else {
            if (thissum < 0){
                s = i + 1;
                thissum = 0;
            }
        }
    }
    cout<<maxsum<<' '<<number[start]<<' '<<number[tend]<<endl;

}

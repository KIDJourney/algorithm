#include<iostream>
#include<map>
#include<stdio.h>
using namespace std;
main()
{
    int n;
    cin>>n;
    map<int,double> numset;
    for (int i = 0 ; i < n ; i++){
        int exp ;
        double coe;
        cin>>exp>>coe;
        if ( numset.find(exp) == numset.end()){
            numset[exp] = coe;
        } else {
            numset[exp] += coe;
        }
    }
    cin>>n;
    for (int i = 0 ; i < n ; i++){
        int exp ;
        double coe;
        cin>>exp>>coe;
        if ( numset.find(exp) == numset.end()){
            numset[exp] = coe;
        } else {
            numset[exp] += coe;
        }
    }
    int num = 0;
    for (std::map<int,double>::reverse_iterator  iter = numset.rbegin() ; iter != numset.rend() ; iter ++){
        if (iter->second != 0){
            num ++;
        }
    }
    cout<<num;
    for (std::map<int,double>::reverse_iterator iter = numset.rbegin() ; iter != numset.rend() ; iter ++){
        if (iter->second != 0){
            printf(" %d %.1lf", iter->first , iter->second);
        }
    }


}

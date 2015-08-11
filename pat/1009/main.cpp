#include<iostream>
#include<map>
#include<stdio.h>
using namespace std;
main()
{
    int n1,n2;
    cin>>n1;
    map<long long , double> numset;
    map<long long , double> ans;
    for (int i = 0 ; i < n1 ; i++){
        int exp;
        double coe;
        cin>>exp>>coe;
        numset[exp] = coe;
    }
    cin>>n2;
    for (int i = 0 ; i < n2 ; i++){
        int exp;
        double coe;
        cin>>exp>>coe;
        for(std::map<long long,double>::iterator iter = numset.begin() ; iter != numset.end() ; iter ++){
            int newexp = iter->first + exp;
            double newcoe = iter->second * coe;
            if(ans.find(newexp) != ans.end()){
                ans[newexp] += newcoe;
            } else {
                ans[newexp] = newcoe;
            }
        }
    }

    printf("%d",ans.size());
    for(std::map<long long,double>::reverse_iterator iter = ans.rbegin() ; iter != ans.rend() ; iter ++){
        printf(" %d %.1lf",iter->first,iter->second);
    }


}

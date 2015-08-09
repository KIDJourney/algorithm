#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
    int chrnum[1000050];
    char chr[1000050];
    int n;
    int len;
    cin>>n;
    for(int i = 0 ; i < n ; i++){
        cin>>len;
        char pre;
        char now;
        int num = 0;
        int pos = 0;
        cin>>now;
        pre = now;
        num = 1;
        pos = 0;
        for (int i = 1 ; i < len ; i++){
            cin>>now;
            if (now == pre){
                num ++ ;
            } else {
                chr[pos] = pre;
                chrnum[pos++] = num;
                num = 1;
                pre = now;
            }
        }
        if (num != 0){
            chr[pos] = now;
            chrnum[pos++] = num;
        }
        int flag = 0;
        for (int i = 0 ; i < pos-2 ; i++){
            if ((chr[i]+1 == chr[i+1] and chr[i+1]+1 == chr[i+2]) and
                (chrnum[i] >= chrnum[i+1] and chrnum[i+1] <= chrnum[i+2])){
                    flag = 1;
                    break;
            }
        }
        if (flag){
            cout<<"YES"<<endl;
        } else {
            cout<<"NO"<<endl;
        }

    }
}

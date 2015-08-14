#include<iostream>
#include<string.h>
#include<string>
using namespace std;
main()
{
    string origin ;
    string doubleorigin;
    cin>>origin;
    int originnum[10] = {0};
    int goalnum[10] = {0};
    int up = 0;
    for(int i = origin.length()-1 ; i >= 0 ; i--){
        originnum[origin[i] - '0'] ++;
        int sum = (origin[i] - '0')*2 + up;
        up = sum / 10;
        doubleorigin += sum % 10 + '0';
    }
    int flag = 1;
    if (origin.length() != doubleorigin.length()){
        cout<<"No"<<endl;
        flag = 0;
    }
    if (up){
        doubleorigin += up + '0';
    }
    for(int i = doubleorigin.length() - 1 ; i >=0 ; i--){
        goalnum[doubleorigin[i] - '0']++;
    }
    for(int i = 0 ; i < 10 ; i++){
        if (originnum[i] != goalnum[i]){
            cout<<"No"<<endl;
            flag = 0;
            break;
        }
    }
    if (flag)
        cout<<"Yes"<<endl;
    for(int i = doubleorigin.length()-1 ; i >= 0 ; i--){
        cout<<doubleorigin[i];
    }
    cout<<endl;

}

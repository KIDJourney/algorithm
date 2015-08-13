#include<iostream>
#include<string>
using namespace std;
string decto13(int in){
    string ret;
    while(in){
        int left = in%13;
        ret += left >= 10 ?left-10+'A':left+'0';
        in/=13;
    }
    if (ret.length() < 2){
        ret = ret + "0";
    }
    if (ret.length() < 2){
        ret = ret + "0";
    }
    return ret;
}
main()
{
    int a;
    cout<<"#";
    while(cin>>a){
        string result = decto13(a);
        cout<<result[1]<<result[0];
    }
}

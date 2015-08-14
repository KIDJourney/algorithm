#include<iostream>
#include<string>
using namespace std;
string add(string str){
    string ret;
    int up = 0;
    for(int s = 0 , e = str.length() - 1 ; e >= 0 ; s ++ , e--){
        int sum = str[s] + str[e] - '0' * 2 + up;
        up = sum / 10;
        ret = char(sum % 10 + '0') + ret;
    }
    if(up){
        ret = char(up + '0') + ret;
    }
    return ret;
}
bool judge(string str){
    for(int s= 0 , e = str.length() -1 ; s <= e ;s++ , e--){
        if (str[s] != str[e]){
            return false;
        }
    }
    return true;
}
main()
{
    string num;
    string rnum;
    int time;
    cin>>num>>time;
    for(int i = 0 ; i < time ; i++){
        if (judge(num)){
            cout<<num<<endl;
            cout<<i;
            break;
        }
        num = add(num);
        if (i == time - 1){
            cout<<num<<endl;
            cout<<i+1;
            break;
        }
    }
}

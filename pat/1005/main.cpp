#include<iostream>
#include<string>
#include<sstream>
#include<string>
using namespace std;
main()
{
    string number[10] = {"zero","one","two","three","four",
                         "five","six","seven","eight","nine"};
    long long sum = 0;
    char input;
    while(cin>>input){
        sum += input - '0';
    }
    stringstream ss;
    string num ;
    ss << sum;
    ss >> num;
    cout<<number[num[0] - '0'];
    for (int i = 1, len = num.length() ; i < len ; i++){
        cout<<' '<<number[num[i] - '0'];
    }

}

#include<iostream>
#include<string>
#include<sstream>
using namespace std;
main()
{
  int a , b;
  while(cin>>a>>b){
    int sum = a + b;
    string ans = "";
    if (sum < 0){
      ans += "-";
      sum = sum * -1;
    }
    stringstream ss ;
    string temp;
    ss << sum;
    ss >> temp;
    string reverse = "";
    for (int i = temp.length() -1 , count = 0; i >= 0 ; i-- , count ++){
      if (count %3 == 0 and count){
        reverse += ",";
      }
      reverse += temp[i];

    }
    cout<<ans;
    for (int i = reverse.length()-1; i >= 0 ; i-- ){
      cout<<reverse[i];
    }
    cout<<endl;
  }
}

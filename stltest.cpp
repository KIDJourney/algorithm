#include<iostream>
#include<map>
using namespace std;
main()
{
    map <string,int> mymap;
    mymap.insert(map<string,int>::value_type("wsy",23));//insert不覆盖
    mymap["kd"]=23;//数组赋数值会覆盖。
    mymap["kd"]=25;
    mymap["ks"]=24;
    for (auto i = mymap.begin();i!=mymap.end();i++)
    {
        cout<<"key ="<<i->first<< " value = "<<i->second<<endl;
    }
}

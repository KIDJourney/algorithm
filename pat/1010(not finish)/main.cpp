#include<iostream>
#include<string>
using namespace std;
int char2num(char c)
{
    if (c<='9'&&c>='0'){
        return c-'0';
    } else {
        return c-'a'+10;
    }
}

long long string2num(string s , long long base)
{
    long long tempbase = 1;
    long long value = 0;
    for(string::reverse_iterator iter = s.rbegin() ;
        iter < s.rend() ; iter++){
            value += tempbase * char2num(*iter);
            tempbase *= base;
        }
    return value;
}

long long findans(string give , int goal)
{
    long long high = goal + 1;
    long long low = 2;
    for (int i = 0 , value , len = give.length() ; i < len ; i++){
        value = char2num(give[i]);
        if (value >= low){
            low = value + 1;
        }
    }
    while (low <= high){
        long long base = (low + high) / 2;
        long long value = string2num(give,base);
        if (value == goal){
            return base;
        }
        if (value > goal){
            high = base - 1;
        } else {
            low = base + 1;
        }
    }
    return 0;
}
int main()
{
    string give ;
    string know;
    long long goal;
    int radix;
    int tag;
    cin>>know>>give>>tag>>radix;
    if (know == give && know == "1"){
        cout<<2<<endl;
        return 0 ;
    }
    if (know == give && know != "1"){
        cout<<radix<<endl;
        return 0 ;
    }
    if (tag == 2){
        swap(know,give);
    }
    goal = string2num(know , radix);
    long long result = findans(give,goal);
    if (result){
        cout<<result<<endl;
    } else {
        cout<<"Impossible"<<endl;
    }
}

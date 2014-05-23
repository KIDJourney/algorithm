#include<string>
#include<iostream>
#include<algorithm>
using namespace std;
main()
{
    string word="BCG";
    while (next_permutation(word.begin(),word.end()))
        cout<<word<<endl;
}

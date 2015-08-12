#include<iostream>
#include<stdio.h>
using namespace std;
main()
{

double ans = 1;
double a ,b ,c;
for(int i = 0 ; i < 3 ; i++){
	cin>>a>>b>>c;
    cout<< (a>b?(a>c?'W':'L'):(b>c?'T':'L'));
    cout<<' ';
    ans *= max(a,max(b,c));
}
    ans = ans * 1.3 - 2;
    printf("%.2lf",ans);

}

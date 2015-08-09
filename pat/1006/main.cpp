#include<iostream>
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
main()
{
    string first ;
    string last;
    int n;
    cin>>n;
    int sh , sm , ss , eh , em , es;
    cin>>first;
    last = first;
    scanf("%d:%d:%d %d:%d:%d",&sh,&sm,&ss,&eh,&em,&es);
    for (int i = 1 ; i < n ; i++){
        string name;
        int h,m,s;
        cin>>name;
        scanf("%d:%d:%d",&h,&m,&s);
        bool flag = 0;
        if (h != sh){
            if (h < sh){
                flag = 1;
            }
        } else if(m != sm ){
            if (m < sm){
                flag = 1;
            }
        } else if(s != ss){
            if (s < sm){
                flag = 1;
            }
        }
        if (flag){
            sh = h;
            sm = m;
            ss = s;
            first = name;
        }
        scanf("%d:%d:%d",&h,&m,&s);
        flag = 0;
        if (h != eh){
            if (h > eh){
                flag = 1;
            }
        } else if(m != em ){
            if (m > em){
                flag = 1;
            }
        } else if(s != es){
            if (s > em){
                flag = 1;
            }
        }
        if (flag){
            eh = h;
            em = m;
            es = s;
            last = name;
        }
    }
    cout<<first<<' '<<last;

}

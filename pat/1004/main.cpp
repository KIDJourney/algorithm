#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
bool map[105][105];
int ans[105];
int num ;
void dfs(int pos,int level){
    if (ans[level] == -1){
        ans[level] = 0;
    }
    bool flag = 0;
    for (int i = 1 ; i < num + 1 ; i ++){
        if (map[pos][i]){
            flag = 1;
            dfs(i,level+1);
        }
    }
    if (!flag)
        ans[level] ++;
}
main()
{
    int non_leaf;
    cin>>num>>non_leaf;
    memset(map,0,sizeof(map[0][0])*105*105);
    memset(ans,-1,sizeof(ans));
    for(int i = 0 ; i < non_leaf ; i++){
        int parent , k , kids;
        cin>>parent>>k;
        for (int i = 0 ; i < k ; i++){
            cin>>kids ;
            map[parent][kids] = 1;
        }
    }
    dfs(1,0);
    cout<<ans[0];
    for(int i = 1 ; ans[i] != -1 ; i ++){
            cout<<' '<<ans[i];
    }
}

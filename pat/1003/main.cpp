#include<iostream>
#include<string.h>
#define MAX 605
using namespace std;
int map[MAX][MAX];
int visit[MAX];
int value[MAX];
int minlen = -1;
int maxvalue = 0;
int pathnum = 0;
int posend;
int citynum;
void dfs(int pos , int step , int tval)
{
    if (visit[pos])
        return;
    if (pos == posend){
        if (step<minlen || minlen == -1){
            minlen = step;
            maxvalue = tval ;
            pathnum = 1;
        } else if (step == minlen){
            maxvalue = max(tval, maxvalue);
            pathnum ++;
        }
        return;
    }
    if (step > minlen && minlen != -1){
        return;
    }
    visit[pos] = 1;
    for (int i = 0 ; i < citynum ; i++){
        if (map[pos][i] && visit[i] != 1){
            dfs(i,step+map[pos][i],tval + value[i]);
        }
    }
    visit[pos] = 0;
}
main()
{
    int start,roadnum;
    cin>>citynum>>roadnum>>start>>posend;
    memset(map,0,sizeof(map[0][0])*MAX*MAX);
    memset(visit,0,sizeof(visit));
    memset(value,0,sizeof(value));
    for(int i = 0 ; i < citynum ; i++){
        cin>>value[i];
    }
    for (int i = 0 ; i < roadnum ; i++){
        int s, e;
        cin>>s>>e;
        cin>>map[s][e];
        map[e][s] = map[s][e];
    }
    dfs(start,0,value[start]);
    cout<<pathnum<<' ';
    cout<<maxvalue<<endl;

}

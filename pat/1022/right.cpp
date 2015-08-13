#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<sstream>
using namespace std;

int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        //build map
        map<string,std::vector<string> > queryMap[5];
        while(n--)
        {
            getchar();
            string id, title, author, wordList, publisher, year;
            getline(cin, id);
            getline(cin, title);
            getline(cin, author);
            getline(cin, wordList);
            getline(cin, publisher);
            cin>>year;
            queryMap[0][title].push_back(id);
            queryMap[1][author].push_back(id);
            queryMap[3][publisher].push_back(id);
            queryMap[4][year].push_back(id);
            istringstream istr(wordList);
            while(!istr.eof())
            {
                string word;
                istr>>word;
                queryMap[2][word].push_back(id);
            }
        }
        //sort first
        for(int i = 0; i < 5; ++i)
        {
            map<string,std::vector<string> > ::iterator it;
            for(it=queryMap[i].begin(); it!=queryMap[i].end(); it++)
                sort(it->second.begin(), it->second.end());
        }
        //query
        int m;
        scanf("%d",&m);
        while(m--)
        {
            int index;
            string q;
            scanf("%d: ", &index);
            getline(cin, q);
            printf("%d: ", index);
            cout<<q<<endl;
            index--;
            map<string,std::vector<string> >::iterator it;
            it = queryMap[index].find(q);
            if(it!=queryMap[index].end())
            {
                std::vector<string> result = queryMap[index][q];
                for(int i = 0; i < result.size(); ++i)
                    cout<<result[i]<<endl;
            }
            else printf("Not Found\n");

        }
    }
    return 0;
}

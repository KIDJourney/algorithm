#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<map>
#include<sstream>
using namespace std;
main()
{
    int n;
    while(scanf("%d",&n) != EOF)
    {
        map<string , vector<string> > querymap[5];
        while(n--)
        {
            getchar();
            string id , title , author , wordlist ,publisher , year;
            getline(cin,id);
            getline(cin,title);
            getline(cin,author);
            getline(cin,wordlist);
            getline(cin,publisher);
            cin>>year;
            querymap[0][title].push_back(id);
            querymap[1][author].push_back(id);
            querymap[3][publisher].push_back(id);
            querymap[4][year].push_back(id);
            istringstream istr(wordlist);
            while(!istr.eof())
            {
                string word;
                istr >> word;
                querymap[2][word].push_back(id);
            }
        }
        for (int i = 0 ; i < 5 ; i ++)
        {
            map<string , vector<string> >::iterator iter;
            for(iter = querymap[i].begin() ; iter != querymap[i].end(); iter ++)
            {
                sort(iter->second.begin(),iter->second.end());
            }
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
                it = querymap[index].find(q);
                if(it!=querymap[index].end())
                {
                    std::vector<string> result = querymap[index][q];
                    for(int i = 0; i < result.size(); ++i)
                        cout<<result[i]<<endl;
                }
                else printf("Not Found\n");



            }

        }

    }


}

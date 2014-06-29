/*************************************************************************
	> File Name: 3295.cpp
	> Author: ma6174
	> Mail: ma6174@163.com
	> Created Time: 2014年06月29日 星期日 21时20分05秒
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int state[5];
char s[205];
int l=0;
int ind()
{
	char ch=s[l++];
	printf("");

	switch(ch)
	{
	case 'p':
	case 'q':
	case 'r':
	case 's':
	case 't':
		return state[ch-'p'];
		break;
	case 'K':
		return ind()&ind();
		break;
	case 'A':
		return ind()|ind();
		break;
	case 'N':
		return !ind();
		break;
	case 'C':
		return !ind()|ind();
		break;
	case 'E':
		return ind()==ind();
		break;
	}
}

int main()
{
    scanf("%s", s);
    while(s[0]!='0')
    {
        int len=strlen(s);
        int mark=1;
        for(state[0]=0; state[0]<=1 && mark; state[0]++)
        {
            for(state[1]=0; state[1]<=1 && mark; state[1]++)
            {
                for(state[2]=0; state[2]<=1 && mark; state[2]++)
                {
                    for(state[3]=0; state[3]<=1 && mark; state[3]++)
                    {
                        for(state[4]=0; state[4]<=1 && mark; state[4]++)
                        {
			    l=0;
                            if(ind()==0)
                               mark=0;
                        }
                    }
                 }
            }
        }
        if(mark==1)
            printf("tautology\n");
        else
            printf("not\n");
        scanf("%s", s);
    }
    return 0;
}

//这种方法太巧妙了！！！！！！
//膜拜Orz！！！！

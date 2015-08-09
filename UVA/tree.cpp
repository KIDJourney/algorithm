#include<iostream>
using namespace std;
struct rode{
    rode * left;
    rode * right;
    int value;
    rode()
    {
        value = 0;
        left=NULL;
        right=NULL;
    }
};
rode * build()
{
    rode * now ;
    char num;
    scanf("%c",&num);
    if (num=='#')
        return NULL;
    now = new rode;
    now->value = num-'0';
    now->left = build();
    now->right = build();
}
main()

{
}


//8ms      2010-05-14 15:09:52
 //ac(1)
//Type:  string Palindromes (回文串数)
//数据规模比较小，暴力解决
//注意判重
#include <stdio.h>
#include <string.h>
#define NL 100

char s[NL];
char palin[NL][NL*NL];
int np;

bool ispalin(int i, int j)
{
    char s0[NL];
    int K = 0, i0, j0;
    i0 = i;
    j0 = j;
    while (i0<=j0) {
        if (s[i0] != s[j0]) return false;
        i0++;
        j0--;
    }
    i0 = i;
    j0 = j;
    while (i0<=j0) {
        s0[K++] = s[i0++];
    }
    s0[K] = '\0';
    for (K=0; K<np; K++) {
        if (!strcmp(s0, palin[K])) return false;
    }
    strcpy(palin[np], s0);
    np++;
    return true;
}

int main()
{
    int len, i, j;
    while (gets(s)) {
        len = strlen(s);
        if (len == 0) continue;
        int cnt = 0;
        np = 0;
        for (i=0; i<len; i++) {
            for (j=i; j<len; j++) {
                if (ispalin(i, j)) {
                    cnt++;
                }
            }
        }
        printf("The string '%s' contains %d palindromes.\n", s, cnt);
    }
    return 0;
}

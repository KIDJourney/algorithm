#include <iostream>
#include<string>
using namespace std;
int main(void)
{
    string pClrs[6] = { "BCG", "BGC", "CBG", "CGB", "GBC", "GCB"};
    for (int n[3][3], aMove[6], nMin, i; cin >> n[0][0];)
    {

        cin >> n[0][1] >> n[0][2] >> n[1][0] >> n[1][1];
        cin >> n[1][2] >> n[2][0] >> n[2][1] >> n[2][2];
        aMove[0] = n[1][0] + n[2][0] + n[0][2] + n[2][2] + n[0][1] + n[1][1];
        aMove[1] = n[1][0] + n[2][0] + n[0][1] + n[2][1] + n[0][2] + n[1][2];
        aMove[2] = n[1][2] + n[2][2] + n[0][0] + n[2][0] + n[0][1] + n[1][1];
        aMove[3] = n[1][2] + n[2][2] + n[0][1] + n[2][1] + n[0][0] + n[1][0];
        aMove[4] = n[1][1] + n[2][1] + n[0][0] + n[2][0] + n[0][2] + n[1][2];
        aMove[5] = n[1][1] + n[2][1] + n[0][2] + n[2][2] + n[0][0] + n[1][0];
        for (nMin = i = 0; ++i < 6; nMin = aMove[i] < aMove[nMin] ? i : nMin);
        cout << pClrs[nMin] << ' ' << aMove[nMin] << endl;
    }
    return 0;
}
//挺简单一个题，我想太多了。

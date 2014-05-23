#include <iostream>
#include <cmath>
using namespace std;
main()
{
    double H,M, N,K;
    while (cin>>H>>M)
    {
        if (H==0 || H==0) return 0;
        N =1;
        while (abs(log(N)/log(N+1) -log(M)/log(H)) >1e-10)
            ++N;
        K=int(0.5+log(H)/log(N+1));
        if (int(N) ==1) cout<<int(K);
        else cout<<int(0.5+ (1-pow(N,K)) / (1- N) );
        cout<<' '<<int(0.5+ (1-pow(N/(N+1),K+1)) * (N+1) *H ) <<endl;
    }
}
/*无法直视的数学题
最反感这种卡精度的数学题。
推导得到高度变化为
H H/(n+1) h/(n+1)^2 ...... h/(n+1)^k
数量变化为
1 n n^2 ........ n^k
连立得 (h/m)=(n+1)^k/n^k
得 ln(h)/ln(m)=ln(n+1)/ln(n)=k
控制精度枚举n
*/

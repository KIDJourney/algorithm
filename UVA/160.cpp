#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int prime[ 105 ];
int table[ 105 ];
int ouput[ 105 ];

int main()
{
	//计算素数、筛法打表
	memset( table, 0 , sizeof(table) );
	int count = 0;
	for ( int i = 2 ; i <= 101 ; ++ i )
		if ( !table[i] ) {
			prime[count ++] = i;
			for ( int j = 2*i ; j <= 101 ; j += i )
				table[j] = 1;
		}

	int n;
	while ( scanf("%d",&n) && n ) {
		memset( ouput, 0, sizeof(ouput) );
		for ( int i = 2 ; i <= n ; ++ i ) {
			int m = i,now = 0;
			while ( m > 1 ) {
				while ( m%prime[now] == 0 ) {
					m /= prime[now];
					ouput[now] ++;
				}
				now ++;
			}
		}
		printf("%3d! =",n);
		for ( int i = 0 ; prime[i] <= n ; ++ i ) {
			printf("%3d",ouput[i]);
			if ( (i+1)%15 == 0 ) {
				printf("\n");
				if ( prime[i+1] <= n )
					printf("      ");
			}
		}
		if ( prime[14] > n || prime[15] <= n )
			 printf("\n");
	}
	return 0;
}

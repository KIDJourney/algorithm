#include <cstdio>
#include <cstring>
#define MAX 105

int dx[4] = {0, -1, 0, 1}, dy[4] = {1, 0, -1, 0};
int a, b, n, m, map[MAX][MAX], sta[MAX][3];
int dir(char c){switch(c){case 'N': return 0; case 'W': return 1; case 'S': return 2; default: return 3;}}

int main() {
	int T, i, j, x, y, suc;
	char ts[5];
	//freopen("input.txt", "r", stdin);
	scanf("%d", &T);
	while(T--) {
		memset(map, 0, sizeof(map));
		scanf("%d%d%d%d", &a, &b, &n, &m);
		for(i = 1; i <= n; i++) {
			scanf("%d%d%s", &x, &y, ts);
			map[x][y] = i;
			sta[i][0] = x, sta[i][1] = y, sta[i][2] = dir(ts[0]); 
		}
		suc = 1;
		while(m--) {
			scanf("%d%s%d", &i, ts, &j);
			while(j-- && suc)
				switch(ts[0]){
					case 'L':
						sta[i][2] = (sta[i][2] + 1) % 4;
						break;
					case 'R':
						sta[i][2] = (sta[i][2] + 3) % 4;
						break;
					default:
						map[sta[i][0]][sta[i][1]]  = 0;
						x = sta[i][0] += dx[sta[i][2]];
						y = sta[i][1] += dy[sta[i][2]];
						if(!x || x > a || !y || y > b) {
							printf("Robot %d crashes into the wall\n", i);
							suc = 0;
						}
						else if(map[x][y]) {
							printf("Robot %d crashes into robot %d\n", i, map[x][y]);
							suc = 0;
						}
						else
							map[x][y] = i;
						break;
				}
		}
		if(suc)
			printf("OK\n");
	}
	return 0;
}

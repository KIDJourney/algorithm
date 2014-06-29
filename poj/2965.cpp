#include<iostream>
using namespace std;
int handle[5][5],ways[17][2];
int k,l;
int judge()
{
	int i,j,sum=0;
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			sum+=handle[i][j];
		if(sum==16) return 1;
		return 0;
}
void convert(int i,int j)
{
	int kk;
	handle[i][j]^=1;
	for(kk=1;kk<=4;kk++)
	{
		handle[i][kk]^=1;
		handle[kk][j]^=1;
	}
}
void dfs(int ii,int jj,int now,int total,int ll)//现在到ii,jj开关了，翻转了now次，总共翻转了total次。
{
	int i,j;
	if(now==total)
	{
		k=judge();
		l=ll;
		return;
	}
	for(i=ii;i<=4;i++)//注意转换，行不变，第一次jj向后移一位，以后从1开始。
	{
		if(i==ii) j=jj+1;
		else j=1;
		for(;j<=4;j++)
		{
			ways[ll][0]=i;
			ways[ll][1]=j;
			convert(i,j);
			dfs(i,j,now+1,total,ll+1);
			if(k) return;
			convert(i,j);//还原。
		}
	}
}
int main()
{
	int i,j;
	char ch;
	for(i=1;i<=4;i++)//输入，用0代替w，用1代替b。
		for(j=1;j<=4;j++)
		{
			cin>>ch;
			if(ch=='+') handle[i][j]=0;
			else handle[i][j]=1;
		}
		cout<<endl;
		for(i=1;i<=16;i++)//最多翻转16次，枚举。
		{
			k=0;
			dfs(1,0,0,i,1);//起点（1,0）
			if(k) break;
		}
		cout<<i<<endl;
		for(i=1;i<=l-1;i++)
			cout<<ways[i][0]<<' '<<ways[i][1]<<endl;
		return 0;
}

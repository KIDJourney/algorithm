

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        if len(stoneValue) <= 1:
            return 0

        self.m = 0
        size = len(stoneValue)

        self.dp = [[0 for i in range(size)]
                   for j in range(size)]

        pre_sum = [stoneValue[0]]
        for idx in range(1, size):
            pre_sum.append(pre_sum[idx - 1] + stoneValue[idx])
        self.pre_sum = pre_sum

        self.dp_solve(0, size - 1)

        return self.m

    def get_sum(self, i, j):
        if i == 0:
            return self.pre_sum[j]
        else:
            return self.pre_sum[j] - self.pre_sum[i - 1]

    def dp_solve(self, i, j):
        if i == j:
            return 0
        if self.dp[i][j]:
            return self.dp[i][j]

        for idx in range(i, j):
            left_sum = self.get_sum(i, idx)
            right_sum = self.get_sum(idx + 1, j)

            left_dp = self.dp_solve(i, idx) + self.get_sum(i, idx)
            right_dp = self.dp_solve(idx + 1, j) + self.get_sum(idx + 1, j)

            if left_sum == right_sum:
                self.dp[i][j] = max(self.dp[i][j], max(left_dp, right_dp))
            else:
                if left_sum < right_sum:
                    self.dp[i][j] = max(
                        self.dp[i][j], left_dp)
                else:
                    self.dp[i][j] = max(
                        self.dp[i][j], right_dp)

        self.m = max(self.m, self.dp[i][j])
        return self.dp[i][j]


s = Solution()
print(s.stoneGameV([6, 2, 3, 4, 5, 5]))
print(s.stoneGameV([7, 7, 7, 7, 7, 7, 7]))
print(s.stoneGameV([4]))

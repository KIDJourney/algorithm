class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if not arr:
            return 0
        if len(arr) == 1:
            return min(arr)

        width = len(arr[0])
        height = len(arr)

        dp = [[1e8 for _ in i] for i in arr]
        for i in range(width):
            dp[0][i] = arr[0][i]
        for row_num in range(1, height):
            for col_num in range(width):
                for last_col_num in range(width):
                    if col_num != last_col_num:
                        dp[row_num][col_num] = min(dp[row_num - 1][last_col_num] + arr[row_num][col_num],
                                                   dp[row_num][col_num])

        return min(dp[-1])


s = Solution()
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.minFallingPathSum(arr))

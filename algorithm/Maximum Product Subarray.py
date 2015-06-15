class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        dp = [[0 for _ in range(len(nums))] , [0 for _ in range(len(nums))]]
        dp[0][1] = nums[0]
        dp[0][0] = 1
        for i in range(len(nums))[1:] :
            dp[i][1] = max(nums[i],nums[i]*dp[i-1][])

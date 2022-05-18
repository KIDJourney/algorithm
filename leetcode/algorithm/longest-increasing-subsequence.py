class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)

        for idx in range(len(nums)):
            for j in range(idx + 1, len(nums)):
                if nums[j] > nums[idx]:
                    dp[j] = max(dp[j], dp[idx] + 1)

        return max(dp)


s = Solution()
for k in [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3], [7, 7, 7, 7, 7, 7, 7]]:
    print(s.lengthOfLIS(k))

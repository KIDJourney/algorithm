class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        now = 0

        for i in nums :
            now += i 
            ans = max(now , ans)
            if now < 0 :
                now = 0

        return ans

job = Solution()
print(job.maxSubArray([-1]))
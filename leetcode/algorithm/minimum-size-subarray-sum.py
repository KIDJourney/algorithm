class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        num_sum = 0
        start = 0
        min_len = len(nums) + 1
        for i,value in enumerate(range(len(nums))):
            num_sum += nums[i]
            while num_sum >= s:
                min_len = min(min_len, i -start + 1 )
                num_sum -= nums[start]
                start += 1
        if min_len == len(nums) + 1:
            return 0 
        else :
            return min_len
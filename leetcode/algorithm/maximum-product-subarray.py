class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ret = nums[0]
        max_l = [nums[0]]
        min_l = [nums[0]]

        for i in range(1, len(nums)):
            max_now = max((max_l[i - 1] * nums[i], min_l[i - 1] * nums[i], nums[i]))
            min_now = min((max_l[i - 1] * nums[i], min_l[i - 1] * nums[i], nums[i]))
            ret = max(ret, max_now)
            max_l.append(max_now)
            min_l.append(min_now)

        return ret

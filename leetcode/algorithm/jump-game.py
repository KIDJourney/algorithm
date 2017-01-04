class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0
        reach = 0
        reach = max(index + nums[index], reach)
        while index < len(nums) and index <= reach:
            reach = max(index + nums[index], reach)
            index += 1

        return index == len(nums)            
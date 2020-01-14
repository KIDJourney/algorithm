class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        s = 0
        e = len(nums) - 1
        while s <= len(nums) - 1 and nums[s] == sorted_nums[s]:
            s += 1

        while e >= 0 and nums[e] == sorted_nums[e]:
            e -= 1

        res = max(e - s + 1, 0)

        return res

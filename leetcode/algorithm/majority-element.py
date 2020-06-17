class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        mc = 1
        for i in nums:
            if mc == 0:
                m = i
                mc = 1
            elif m == i:
                mc += 1
            else:
                mc -= 1

        return mc

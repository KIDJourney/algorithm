class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                ret.append(abs(x))
            else :
                nums[abs(x) - 1] *= -1
        
        return ret
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i , j = 0 , 0
        for i in range(0,len(nums)):
            if (nums[i]):
                nums[i] , nums[j] = nums[j] , nums[i]
                j += 1


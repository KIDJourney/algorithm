class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        available = {}
        for index , num in enumerate(nums):
            if num in available :
                return [available[num] , index]
            else :
                available[target-num] = index

job = Solution()
print(job.twoSum([0,4,3,0] , 0))

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [(nums[i], i) for i in range(len(nums))]
        nums = list(sorted(nums,key=lambda x: x[0]))
        print(nums)


s = Solution()
s.countSmaller([5, 2, 6, 1])

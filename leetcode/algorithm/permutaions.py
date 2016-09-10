class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.ans = []
        self.generate(nums, [])
        return self.ans

    def generate(self, nums, result):
        if not nums:
            self.ans.append(result)
        for index in range(len(nums)):
            if index + 1 < len(nums) and nums[index] == nums[index+1]:
                continue
            else :
                self.generate(nums[:index] + nums[index+1:], result + [nums[index]])


s = Solution()
print(s.permute([1,2,3]))
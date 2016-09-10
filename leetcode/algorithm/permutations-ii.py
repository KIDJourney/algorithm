class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.generate(nums, [])
        return list(set(self.ans))


    def generate(self, nums, result):
        if not nums :
            self.ans.append(tuple(result))
        origin_result = result[::]
        for index in range(len(nums)) :
            result = result + [nums[index]]
            self.generate([nums[i] for i in range(len(nums)) if i != index] , result)
            result = origin_result[::]

s = Solution()
print(s.permuteUnique([1,2,3,4]))
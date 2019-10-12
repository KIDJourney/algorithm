class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        nums = sorted(nums, reverse=True)
        print(nums)

        return ''.join(nums)


s = Solution()
"9534330"
print(s.largestNumber([3, 30, 34, 5, 9]))

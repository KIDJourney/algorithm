class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        mid = nums[len(nums) / 2]

        ret = 0
        for i in nums:
            ret += abs(i - mid)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.minMoves2([10, 10, 10, 10, 10, 10, 10, 10, 1]))

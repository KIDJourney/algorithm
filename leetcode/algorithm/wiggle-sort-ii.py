class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums_copy: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_copy = sorted(nums)
        remain = []
        if len(nums_copy) % 2 == 1:
            remain, nums_copy = [nums_copy[0]], nums_copy[1:]
        step = len(nums_copy) // 2
        ret = []
        for i in range(len(nums_copy) // 2 - 1, -1, -1):
            ret.append(nums_copy[i])
            ret.append(nums_copy[i + step])
        ret = ret + remain

        for i in range(len(nums)):
            nums[i] = ret[i]

        return ret


s = Solution()
print(s.wiggleSort([4, 5, 5, 6]))

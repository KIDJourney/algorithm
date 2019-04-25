class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0

        visit = set()
        for i in nums:
            if i in visit:
                continue

            tmp = 0
            idx = i
            while idx not in visit:
                visit.add(idx)
                tmp += 1
                idx = nums[idx]

            ret = max(ret, tmp)

        return ret


s = Solution()
print(s.arrayNesting([5, 4, 0, 3, 1, 6, 2]))

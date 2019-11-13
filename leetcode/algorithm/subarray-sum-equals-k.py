class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = {0: 1}
        ts = 0
        ret = 0
        for i in nums:
            ts += i
            ret += counter.get(ts - k, 0)
            counter.setdefault(ts, 0)
            counter[ts] += 1

        return ret


s = Solution()

print(s.subarraySum([1, 2, 3], 3))

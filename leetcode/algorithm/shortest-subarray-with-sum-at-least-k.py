class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        prefix_sum = [0]
        pre = 0
        for i in nums:
            if i >= k:
                return 1
            prefix_sum.append(i + pre)
            pre += i

        ans = 60000
        for i in range(len(prefix_sum)):
            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] >= k:
                    ans = min(ans, i - j)

        if ans == 60000:
            return -1
        return ans


s = Solution()
print(s.shortestSubarray([1, 2], 4))

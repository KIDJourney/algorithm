class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        length = len(A)

        first_max = 0

        left, right = 0, 0

        max_sum = 0
        tsum = 0
        while right < length:
            if A[right] + tsum > 0:
                max_sum = max(A[right] + tsum, max_sum)
                if left == 0:
                    first_max = max_sum
            else:
                left = right
                tsum = 0

            right += 1

        if left == 0:
            return max_sum
        else:
            return first_max + max_sum


s = Solution()
print(s.maxSubarraySumCircular([1, -2, 3, -2]))

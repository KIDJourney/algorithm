class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m = max(A)
        mi = min(A)

        if m - mi < 2 * K:
            return 0
        else:
            return m - mi - 2 * K

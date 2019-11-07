class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        r = sorted(map(sorted, dominoes))
        ans = 0
        t = 0
        for i in range(1, len(r)):
            if r[i] == r[i - 1]:
                t += 1
            else:
                ans += for_sum(t)
                t = 0

        if t:
            ans += for_sum(t)

        return ans


def for_sum(n):
    return (1 + n) * n / 2


s = Solution()
print(s.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))

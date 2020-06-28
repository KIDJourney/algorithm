class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        mp = 1
        for i in range(2, n):
            if n % i == 0:
                s = (n // i) ** i
                mp = max(mp, s)
                print(s)
            else:
                tn = n
                p = tn % i
                tn -= p
                sub = tn // i
                s = (sub ** (i - 1)) * (sub + p)
                mp = max(mp, s)
                print(s)

        return mp


s = Solution()

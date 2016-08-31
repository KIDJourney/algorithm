class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 :
            return 0
        f = lambda s : s**2 - x
        df = lambda s : 2*s
        ans = float(x)
        for i in range(200):
            print(ans)
            ans = ans - f(ans) / df(ans)
        return int(ans)

s = Solution()
print(s.mySqrt(2)) 
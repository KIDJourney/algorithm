class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n % 2
        n //= 2
        while n:
            if n % 2 == last:
                return False
            last = n % 2
            n //= 2

        return True


s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))

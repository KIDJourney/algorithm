import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = []
        root = self.find_root(n)
        while n:
            sp = root * root
            while sp < n:
                print(n, sp)
                s.append(sp)
                n -= sp
            root = self.find_root(n)

        return sum(s)

    def find_root(self, n):
        if n == 1:
            return n
        return int(math.sqrt(n))

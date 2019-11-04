class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.num = num
        self.tried = set()
        n = len(self.num)

        return self.check(n - 3, n - 2, n - 1, n)

    def check(self, a, b, c, d):
        if (a, b, c, d) in self.tried:
            return False
        self.tried.add((a, b, c, d))

        if a < 0:
            return False
        
        ta, tb, tc = int(self.num[a:b]), int(self.num[b:c]), int(self.num[c:d])
        if a == 0 and tc - tb == ta:
            return True

        if tc - tb == ta:
            return self.check(a - 1, a, b, c) or self.check(a - 1, b - 1, c, d) or self.check(a - 1, b - 1, c - 1, d)

        return False


s = Solution()
print(s.isAdditiveNumber("199100199"))

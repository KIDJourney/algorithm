# 1 <= d, f <= 30
# 1 <= target <= 1000

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        self.record = {}
        return self.solve(d, f, target)

    def solve(self, d, f, target):
        if d == 0 and target == 0:
            return 1
        elif d == 0 or target < 0:
            return 0

        if (d, target) in self.record:
            return self.record[(d, target)]


        res = 0
        for i in range(1, f + 1):
            res = int((res + self.solve(d - 1, f, target - i)) % (10 ** 9 + 7))

        self.record[(d, target)] = res
        return res


"""
                2 3 4
    1 2 3   1 2 2   1 2 1
    0 2 0    0 2 0      0 2 0    

"""

s = Solution()
print(s.numRollsToTarget(30, 30, 500))

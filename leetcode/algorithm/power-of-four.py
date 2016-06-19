class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bnum = bin(num)
        return bnum[2] == '1' and bnum.count('1') == 1 and bnum[2:].count('0') % 2 == 0


s = Solution()
print(s.isPowerOfFour(16))


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = [1 for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            ans[i] = ans[i-1] if s[i-1] != '0' else 0
            ans[i] += ans[i-2] if i-2 >= 0 and int(s[i-2: i]) > 0 and int(s[i-2:i]) < 27 else 0
        return ans[-1] if len(s) > 0 else 0

s = Solution()
print(s.numDecodings('12'))
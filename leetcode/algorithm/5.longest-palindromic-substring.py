#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for i in range(len(s))]
        max_start, max_len = 0, 0
        n = len(s)

        for start in range(n):
            for end in range(start, n-1):
                if s[start] == s[end]:
                    if end - start <= 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        new_len = end - start + 1
                        if new_len > max_len:
                            max_len = new_len
                            max_start = start

        return s[max_start: max_start + max_len]


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))


# @lc code=end

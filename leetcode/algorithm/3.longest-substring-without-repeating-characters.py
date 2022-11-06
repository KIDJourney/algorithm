#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s_input: str) -> int:
        ans = 0
        s, e = 0, 0
        meet = {}
        while True:
            if e < s:
                e = s
            if e == len(s_input):
                break

            if s_input[e] in meet:
                del meet[s_input[s]]
                s += 1
            else:
                meet[s_input[e]] = True
                ans = max(ans, e-s+1)
                e += 1


        return ans

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))


# @lc code=end

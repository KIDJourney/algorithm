class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        diff = []
        for idx in range(len(s)):
            diff.append(abs(ord(s[idx]) - ord(t[idx])))

        diff = sorted(diff)


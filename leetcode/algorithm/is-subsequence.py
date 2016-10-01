class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        poss = {}
        for index, char in enumerate(t):
            if char in s:
                pos = poss.setdefault(char,[])
                pos.append(index)

        print(poss)


s = Solution()
s.isSubsequence('abc','addbdfca')

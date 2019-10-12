class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = ''.join(S.split('-')).upper()
        extra = len(s) % K

        g = []
        if extra != 0:
            g.append(s[:extra])

        for i in range(extra, len(s), K):
            g.append(s[i:i + K])

        return '-'.join(g)


s = Solution()

print(s.licenseKeyFormatting("1axb-asdf-asq", 2))

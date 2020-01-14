class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = {}
        for c in s:
            counter.setdefault(c, 0)
            counter[c] += 1

        return ''.join([p[0] * p[1] for p in sorted(counter.items(), key=lambda x: -x[1])])


s = Solution()
print(s.frequencySort('tree'))

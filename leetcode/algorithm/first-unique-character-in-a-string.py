class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i in s:
            d.setdefault(i, 0)
            d[i] += 1
        
        for index, value in enumerate(s):
            if d[value] == 1:
                return index
        return -1
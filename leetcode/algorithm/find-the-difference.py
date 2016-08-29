from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_c = Counter(s)
        t_c = Counter(t)
        for key in t_c.keys():
            if key not in s_c:
                return key
            else :
                if s_c[key] != t_c[key]:
                    return key
                
            

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        posg = 0
        poss = 0
        ans = 0

        while posg < len(g) and poss <len(s):
            if g[posg] <= s[poss]:
                posg += 1
                poss += 1
                ans += 1
            else :
                poss+= 1 
        
        return ans
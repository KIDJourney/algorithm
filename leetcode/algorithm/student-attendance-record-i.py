class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        late_too_much = False 
        lastword = ''
        for idx in range(len(s)):
            
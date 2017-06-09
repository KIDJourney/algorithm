from string import digits

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
    def parse(self, expression):
        pos = 0
        while pos < len(expression):
            buffer = ''
            if expression[pos] in digits:
                buffer += expression[pos]
            
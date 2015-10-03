class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valDic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'0':0}
        return sum(valDic[i] if valDic[i] >= valDic[j] else valDic[i]*-1 for i , j in zip(s,(s+'0')[1:]))
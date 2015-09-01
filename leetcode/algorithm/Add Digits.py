class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        numString = str(num)
        while(len(numString) != 1) :

            numSum = 0
            for i in numString : 
                numSum += int(i)
            numString = str(numSum)

        return int(numString)
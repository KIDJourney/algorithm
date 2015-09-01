class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 0 : 
            return False

        prime_factor = [ 2 , 3 , 5 ]

        for i in prime_factor :
            while(num and num % i == 0) :
                num /= i

        if num == 1 : 
            return True
        else :
            return False



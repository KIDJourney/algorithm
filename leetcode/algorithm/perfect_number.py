import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        e = int(math.sqrt(num))
        s = 2
        ss = 1
        while True:
            if s ** 2 == num:
                ss += s
                break
            if s ** 2 > num:
                break
            if num % s == 0:
                ss += s 
                ss += num // s
            s += 1

        return ss == num            
        


if __name__ == "__main__":
    s = Solution()
    assert s.checkPerfectNumber(28) == True
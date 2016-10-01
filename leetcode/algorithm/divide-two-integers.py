max_int = (1 << 31) -1 
min_int = - (1 << 31)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor < 0 :
            divisor = - divisor
            dividend = - dividend

        if dividend > max_int or dividend < min_int:
            return max_int

        ans = 0
        
        if divisor == 0:
            return max_int
        if divisor == 1:
            return dividend

        while dividend >= divisor:
            print(dividend)
            dividend -= divisor
            ans += 1
        
        if ans > max_int or ans < min_int:
            return max_int
        return ans

s = Solution()
print(s.divide(2147483647,2))
def guess(num):
    goal = 1
    if num > goal:
        return 1
    if num < goal:
        return -1
    return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left , right = 1 , n
        mid = (left + right)//2 
        while left < right:
            res = guess(mid)
            if res == 0:
                return mid
            if res == -1:
                right = mid - 1
            if res == 1: 
                left = mid + 1
            mid = (left + right) // 2 
        return mid

s = Solution()
print(s.guessNumber(1))
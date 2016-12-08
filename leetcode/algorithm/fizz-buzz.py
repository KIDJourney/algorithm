class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [('Fizz' if i % 3 == 0 else '') + ('Buzz' if i % 5 == 0 else '') + (str(i) if not (i % 3 == 0 or i % 5 == 0) else '') for i in range(1,n+1)]


s = Solution()
print(s.fizzBuzz(15))
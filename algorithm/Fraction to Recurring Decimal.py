class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0 :
            return str(numerator / denominator)
        ans = []
        step = 0
        while (numerator != 0 and step != 3) :
            ans.append(numerator/denominator)
            numerator = numerator % denominator * 10
            step += 1
        print ans

job = Solution()
job.fractionToDecimal(2,3)

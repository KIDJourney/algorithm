class Solution(object):
    def getSum(self, a, b):
        while b:
            sum = a ^ b
            b = (a & b) << 1
            a = sum         

        return sum


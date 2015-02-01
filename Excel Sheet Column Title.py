class Solution:
    # @return a string
    def convertToTitle(self, num):
        num = num-1
        ans = []
        ans .append(num % 26)
        num /= 26
        while num :
            num -= 1
            ans.append(num%26)
            num/=26
        return ''.join(chr(ord('A')+i) for i in ans[::-1])        
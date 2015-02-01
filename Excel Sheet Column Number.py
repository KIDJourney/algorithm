class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0
        quan = 1
        for i in s[::-1] :
            num += (ord(i) - ord("A") + 1)*quan
            quan*=26
        return num 
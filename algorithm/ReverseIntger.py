class Solution:
    # @return an integer
    def reverse(self, x):
        temp = str(x)
        ans = 0
        if x < 0 :
        	ans = int('-' + (temp[1:])[::-1])
        else :
        	ans = int(temp[::-1])
        return ans
# if you get a num that is less than zero
# then add a '-' and reverse the string
# else just reverse the string
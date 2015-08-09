class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        x = str(x)
        if len(x) <= 1 :
            return True
        s = 0 
        e = len(x) - 1
        while (s < e) :
            if x[s] != x[e] :
                return False
            s += 1
            e -= 1
        return True    
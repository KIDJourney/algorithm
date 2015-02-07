class Solution:
    # @return an integer
    def atoi(self, s):
        s = s.strip()
        if s == "" :
            return 0
        tmp = ''
        numList = map(str,range(10))
        if s[0] in "+-" :
            tmp = s[0]
            s = s[1:]
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        for i in s :
            if i in numList :
                tmp += i 
            else :
                break
        if tmp == "" :
            return 0
        ans = int(tmp)
        if ans > MAX_INT :
            return MAX_INT
        elif ans < MIN_INT :
            return MIN_INT
        return ans 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        step = 0
        ret = ''
        while i >= 0 or j >= 0:
            temp_sum = step
            if i >= 0:
                temp_sum += int(num1[i])
                i -= 1
            if j >= 0:
                temp_sum += int(num2[j])
                j -= 1

            step = temp_sum // 10
            ret = str(temp_sum % 10) + ret

        if step:
            ret = str(step) + ret

        return ret

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowles = 'aeiouAEIOU'
        vowles_index = [i for i in range(len(s)) if s[i] in vowles]

        s = list(s)

        for i in range(len(vowles_index)//2):
            s[vowles_index[i]] , s[vowles_index[-i-1]] = s[vowles_index[-i-1]], s[vowles_index[i]]

        return ''.join(s)

s = Solution()
print(s.reverseVowels('aA'))
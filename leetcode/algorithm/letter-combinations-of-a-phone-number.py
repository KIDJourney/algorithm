import itertools
class Solution(object):
    def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = {'2': 'abc','3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = itertools.product(*[[c for c in mapper[i]] for i in digits])
        return [''.join(a) for a in ans]

s = Solution()
print(s.letterCombinations('23'))
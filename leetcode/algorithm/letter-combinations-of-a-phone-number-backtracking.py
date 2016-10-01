class Solution(object):
    def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = {'2': 'abc','3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return [''.join(ans) for ans in product(*[mapper[i] for i in digits]) if ans]

def product(*args):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

s = Solution()
print(s.letterCombinations('234'))
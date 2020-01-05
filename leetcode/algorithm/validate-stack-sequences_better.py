# pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        temp_stack = []
        idx = 0
        for p in pushed:
            temp_stack.append(p)
            while temp_stack and temp_stack[-1] == popped[idx]:
                temp_stack.pop()
                idx += 1

        return idx == len(popped)


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

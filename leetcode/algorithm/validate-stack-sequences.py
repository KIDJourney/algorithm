# pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        tempStack = []
        i, j = 0, 0

        while i < len(pushed) or j < len(popped):
            if i < len(pushed):
                tempStack.append(pushed[i])
                i += 1

            action = False
            while True:
                if j >= len(popped):
                    break
                if not tempStack:
                    break

                if tempStack[-1] == popped[j]:
                    action = True
                    tempStack.pop()
                    j += 1
                else:
                    break
            if not action and i == len(pushed):
                break

        return i == len(pushed) and j == len(popped)


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

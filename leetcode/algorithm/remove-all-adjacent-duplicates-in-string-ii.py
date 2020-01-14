class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt_stack = []

        for i in s:
            if cnt_stack and cnt_stack[-1][0] == i:
                cnt_stack[-1][1] += 1
            else:
                cnt_stack.append([i, 1])

            if cnt_stack[-1][1] == k:
                cnt_stack.pop()

        return ''.join([i[0] * i[1] for i in cnt_stack])


s = Solution()
print(s.removeDuplicates("deeedbbcccbdaa", 3))

import operator


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        if len(num) == 1:
            if num[0] == target:
                return [str(num[0])]

        self.op_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }

        self.nums = list(map(int, num))
        self.target = target
        self.ret = []

        self.dfs(1, self.nums[0], str(self.nums[0]))

        return self.ret

    def dfs(self, idx, tmp, path=None):
        if idx == len(self.nums):
            if tmp == self.target:
                self.ret.append(path)

            return

        n = self.nums[idx]
        for func in ['+', '-', '*']:
            self.dfs(idx + 1, self.op_map[func](tmp, n), path + func + str(n))


s = Solution()
print(s.addOperators("11", 2))

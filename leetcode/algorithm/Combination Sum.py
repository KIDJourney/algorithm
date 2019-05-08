class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        self.target = target
        self.ans = []

        self.dfs()

        return self.ans

    def dfs(self, s=0, ans=None, pos=0):
        if ans is None:
            ans = []

        if s == self.target:
            self.ans.append(ans)
            return

        for i in range(pos, len(self.candidates)):
            v = self.candidates[i]
            if s + v > self.target:
                return
            ans.append(v)
            self.dfs(s + v, ans=list(ans), pos=i)
            ans.pop()


s = Solution()
print(s.combinationSum([2, 3, 5], 8))

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.ans = 0
        self.m = matrix
        self.global_visit = {}
        self.d = ((1, 0), (0, 1), (-1, 0), (0, -1))

        for x in len(matrix):
            for y in len(matrix[0]):
                dfs(x, y)

        return self.ans

    def valid_xy(self, x, y):
        if not (0 >= x > len(self.m)):
            return False
        if not (0 >= y > len(self.m[0])):
            return False
        return True

    def dfs(self, x, y, visit):
        for d in self.d:
            nx, ny = x + d[0], y + d[1]
            if (nx, ny) in visit:
                continue

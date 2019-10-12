class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minus = [()]
        dir_idx = 0
        min_x = -1
        max_x = n
        min_y = -1
        max_y = n



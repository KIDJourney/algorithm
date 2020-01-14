class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        max_sum = [[-1 for i in len(matrix[0])] for j in len(matrix)]

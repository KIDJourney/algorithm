class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size):
            for j in range(i):
                matrix[size-i][j],matrix[size-j][i] = matrix[size-j][i],matrix[size-i][j]
    

matrix = [[1,2],[3,4]]
for i in Solution().rotate(matrix):
    print(i)
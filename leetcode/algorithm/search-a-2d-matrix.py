import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_index = bisect.bisect_left([i[-1] for i in matrix], target)
        print(row_index)

        if row_index == len(matrix):
            return False


        column_index = bisect.bisect_left(matrix[row_index], target)
        if column_index != len(matrix[row_index]) and matrix[row_index][column_index] == target:
            return True

        return False


s = Solution()
print(s.searchMatrix([[1, 3]],1))
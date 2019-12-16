class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        x, y = 0, 0
        max_x, max_y = len(matrix), 0 if len(matrix) == 0 else len(matrix[0])

        ret = []

        visit = dict()

        def check_pos(tx, ty):
            if tx < 0 or ty < 0 or tx >= max_x or ty >= max_y:
                return False
            if visit.get((tx, ty)):
                return False
            return True

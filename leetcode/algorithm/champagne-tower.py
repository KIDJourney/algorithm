class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        pass


def c(m, n):
    if m == 0 or n == 0:
        return 1
    if m == n:
        return 1

    return reduce(lambda i, j: i * j, range(m - n + 1, m + 1)) // reduce(lambda i, j: i * j, range(1, n + 1))

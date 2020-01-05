class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])

        self.cache = {}
        self.max_g = 0

    def find_grid(self, x, y):
        for i in range(1, min(self.))

    def check_grid(self, x, y, width):
        if x + width >= self.width:
            return False
        if y + width >= self.height:
            return False

        for i in range(x, x + width):
            if self.grid[y][i] != 1:
                return False

        for i in range(y, y + width):
            if self.grid[i][x] != 1:
                return False

        return True

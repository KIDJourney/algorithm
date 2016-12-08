class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.map = grid
        self.height = len(grid)
        self.weight = len(grid[0])

        return self.get_edge()

    def get_edge(self):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        ans = 0
        for row in range(self.height):
            for height in range(self.weight):
                tans = 4
                if self.is_island(row, height):
                    for d in directions:
                        new_row = row + d[0]
                        new_col = height + d[1]
                        if self.is_valid(new_row, new_col) and self.is_island(new_row, new_col):
                            tans -= 1
                    ans += tans
        return ans
                

    def is_valid(self,row,col):
        return 0 <= row < self.height and 0 <= col < self.weight
    
    def is_island(self, row, col):
        return self.map[row][col] == 1

s = Solution()

print(s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
))
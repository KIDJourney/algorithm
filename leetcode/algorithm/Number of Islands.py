#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-19 00:38:23
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-19 16:14:01
class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        ans = 0
        if not grid or not grid[0]:
            return 0

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == '1' :
                    ans += 1
                    self.countLand(i,j,grid)
        return ans


    def countLand(self,i,j,grid):
        if i < 0 or j < 0 or i >=len(grid) or j>=len(grid[0]) or grid[i][j] == '0' :
            return

        grid[i][j] = '0'

        self.countLand(i+1,j,grid)
        self.countLand(i-1,j,grid)
        self.countLand(i,j+1,grid)
        self.countLand(i,j-1,grid)

job = Solution()
job.numIslands([["1","1"]])
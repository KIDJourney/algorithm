class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.board = board
    
    def fill(self,x,y):
        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + d[0]
            ny = y + d[1]
            if self.board[x][y] and  is_valid_pos(nx,ny):
                self.board[x][y] = 
            
    
    def is_valid_pos(self, row,col):
        f1 = 0 <= row < len(self.board)
        f2 = 0 <= col < len(self.board[0])
        return f1 and f2
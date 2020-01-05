class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        board = [[0 for i in range(8)] for j in range(8)]

        for q in queens:
            board[q[0]][q[1]] = 2

        ds = [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1],
            [-1, -1],
            [1, 1],
            [-1, 1],
            [1, -1]
        ]
        ret = []
        for d in ds:
            tx, ty = king[0], king[1]
            while True:
                nx, ny = tx + d[0], ty + d[1]
                if not self.check_pos(nx, ny):
                    break

                if board[nx][ny] == 2:
                    ret.append([nx, ny])
                    break

                tx, ty = nx, ny

        return ret

    def check_pos(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

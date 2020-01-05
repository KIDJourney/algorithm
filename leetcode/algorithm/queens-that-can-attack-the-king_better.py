class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queens = {(i[0], i[1]) for i in queens}

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

                if (nx, ny) in queens:
                    ret.append([nx, ny])
                    break

                tx, ty = nx, ny

        return ret

    def check_pos(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.board_width = len(board)
        self.board_height = len(board[0])

        self.visit = [[0 for _ in range(len(board[0]))]
                      for __ in range(len(board))]

        for row in range(self.board_width):
            for col in range(self.board_height):
                if word[0] == board[row][col]:
                    if self.search((row,col), word[1:]):
                        return True

        return False

    def search(self, pos, word):
        self.visit[pos[0]][pos[1]] = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not word:
            return True

        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if not (0 <= new_pos[0] < self.board_width and 0 <= new_pos[1] < self.board_height and
                    self.board[new_pos[0]][new_pos[1]] == word[0] and self.visit[new_pos[0]][new_pos[1]] != 1):
                continue

            if self.search(new_pos, word[1:]):
                return True

        self.visit[pos[0]][pos[1]] = 0

        return False


s = Solution()
print(s.exist(["CAA","AAA","BCD"], 'AAB'))

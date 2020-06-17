class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        bit_p = {}
        for s in board:
            v = 0
            for c in s:
                v = v | (2 >> (ord(c) - ord('a')))
            bit_p[s] = v

        max_len = 0

        def dfs(start, now, now_bit):
            global max_len
            for i in range(start, len(board)):
                if now_bit & bit_p[board[i]] == 0:
                    new_str = now + board[i]
                    max_len = max(max_len, len(new_str))
                    new_bit = now_bit | bit_p[board[i]]
                    dfs(i + 1, new_str, new_bit)

        return max_len


s = Solution()
s.updateBoard()
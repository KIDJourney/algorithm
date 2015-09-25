class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        blo = [{} for i in range(9)]

        for arow,_ in enumerate(board) :
            for acol,_ in enumerate(board[arow]) :
                character = board[arow][acol]
                if character == '.':
                    continue

                if row[arow].setdefault(character , 0) > 0 :
                    return False
                else :
                    row[arow][character] = 1

                if col[acol].setdefault(character , 0) > 0 :
                    return False
                else :
                    col[acol][character] = 1

                if (blo[int(arow/3)*3+acol/3].setdefault(character,0) > 0) :
                    return False
                else :
                    blo[int(arow/3)*3+acol/3][character] = 1
        return True

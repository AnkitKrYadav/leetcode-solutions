class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col,box = [set() for _ in range (9)], [set() for _ in range (9)], [set() for _ in range (9)]
        for i in range (9):
            for j in range (9):
                if board[i][j] != '.':
                    #row and column validation
                    if board[i][j] in row[i] or  board[i][j] in col[j]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])

                    #box validation
                    n = (i//3) *3 + j//3
                    if board[i][j] in box[n]:
                        return False
                    else:
                        box[n].add(board[i][j])
        return True

                        

                    
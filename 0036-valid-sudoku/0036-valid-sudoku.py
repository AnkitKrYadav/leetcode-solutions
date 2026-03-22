class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col,box = [list() for _ in range (9)], [[] for _ in range (9)], [[] for _ in range (9)]
        for i in range (9):
            for j in range (9):
                if board[i][j] != '.':
                    #row validation
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].append(board[i][j])
                    

                    #col validation
                    if board[i][j] in col[j]:
                        return False
                    else:
                        col[j].append(board[i][j])


                    #box validation
                    n = (i//3) *3 + j//3
                    if board[i][j] in box[n]:
                        return False
                    else:
                        box[n].append(board[i][j])
        return True

                        

                    
class Solution:
    def isValidSudoku(self, board):
        column = [{None} for _ in range (9)]
        row = [{None} for _ in range (9)]
        box = [{None} for _ in range (9)]
        
        for r in range (9):
            for c in range(9):
                val = board[r][c]
                if (val in column[c] or
                    val in row[r] or
                    val in box[c // 3 + (r // 3) * 3]):
                    return False
                
                if (val != '.'):
                    column[c].add(val)
                    row[r].add(val)
                    box[c // 3 + (r // 3) * 3].add(val)
                    
        return True
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["5",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
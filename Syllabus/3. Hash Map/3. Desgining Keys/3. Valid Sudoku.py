from typing import List

def valid_sudoku(board: List[List[str]]) -> bool:
  rows = [set() for _ in range(9)] # List of sets
  columns = [set() for _ in range(9)] # List of sets
  squares = [set() for _ in range(9)] # List of sets

  for row_num in range(len(board)):
    for column_num in range(len(board[0])):
      n = board[row_num][column_num]
      if n == '.':
        continue
      if n in rows[row_num] or n in columns[column_num] or n in squares[row_num // 3 * 3 + column_num // 3]:
        return False
      rows[row_num].add(n)
      columns[column_num].add(n)
      squares[row_num // 3 * 3 + column_num // 3].add(n)
    
  return True
 
print(valid_sudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))
from typing import List

def count_island(grid: List[List[str]]) -> int:
  m = len(grid)
  n = len(grid[0])
  count = 0
  for row in range(m):
    for col in range(n):
      if grid[row][col] == '1':
        count += 1
        dfs(grid, row, col)
  return count

def dfs(grid : List[List[str]], x: int, y: int) -> None:
  stack = [(x,y)]
  while stack:
    row, col = stack.pop()
    grid[row][col] = '0'
    neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    for nb in neighbors:
      if is_valid_neighbor(grid, nb[0], nb[1]):
        stack.append(nb)

def is_valid_neighbor(grid: List[List[str]], row: int, col: int) -> bool:
  return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1'

print(count_island( [
 ["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]
]

))
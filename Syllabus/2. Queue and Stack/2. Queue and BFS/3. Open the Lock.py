from collections import deque
import copy
from typing import List, Set

def open_the_lock(deadends: List[str], target: str) -> int:
  grid = [[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
  visited = set()

  for deadend in deadends:
    a, b, c, d = int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])
    grid[a][b][c][d] = 1
  target = [int(target[0]), int(target[1]), int(target[2]), int(target[3])]
  
  q = deque()
  q.append(([0,0,0,0], 0))

  while q:
    comb, moves = q.popleft()
    visited.add("".join(str(i) for i in comb))
    if comb == target:
      return moves
    neighbors = find_neighbors(grid, comb)
    for neighbor in neighbors:
      if "".join(str(i) for i in comb) not in visited:
        q.append([neighbor, moves + 1])
  
  return -1

def find_neighbors(grid, comb: List[int]):
  neighbors = []
  for i in range(4):
    up = copy.deepcopy(comb)
    up[i] = (up[i] + 1) % 10
    down = copy.deepcopy(comb)
    down[i] = (down[i] - 1) % 10
    
    if grid[up[0]][up[1]][up[2]][up[3]] != 1:
      neighbors.append(up)
    if grid[down[0]][down[1]][down[2]][down[3]] != 1:
      neighbors.append(down) 

  return neighbors

print(open_the_lock( ["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))

from collections import deque
from typing import List, Tuple, Set

def WallsnGates(rooms: List[List[int]]) -> None:
  for row in range(len(rooms)):
    for col in range(len(rooms[0])):
      visited = set()
      q = deque()
      if rooms[row][col] == 2147483647:
        q.append((row, col))
      
      while q:
        i, j = q.popleft()
        visited.add((i, j))
        if rooms[i][j] == 0:
          rooms[row][col] = abs(row - i) + abs(col - j)
          break
        elif rooms[i][j] != -1:
          nbs = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
          for nb in nbs:
            if is_valid_neighbor(nb, visited, rooms):
              q.append(nb)

def is_valid_neighbor(nb: Tuple, visited: Set, rooms: List[List[int]]) -> bool:
    row, col = nb
    return row >= 0 and row < len(rooms) and col >= 0 and col < len(rooms[0]) and rooms[row][col] != -1 and (nb not in visited)
    
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
WallsnGates(rooms)
print(rooms)
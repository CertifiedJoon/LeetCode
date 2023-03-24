from collections import deque
import typing

def WallsnGates(rooms: List[List[int]]) -> None:
  for row in range(len(rooms)):
    for col in range(len(rooms)):
      visited = set()
      q = deque()
      if rooms[row][col] == 0:
        q.append((row, col))
      
      while q:
        i, j = q.popleft()
        visited.add((i, j))
        if rooms[i][j] == 0:
          rooms[row][col] == abs(row - i) + abs(col - j)
          break
        elif rooms[i][j] != -1:
          nbs = ((i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1))
          for nb in nbs:
            if is_valid_neighbor(nb, visited, rooms):
              q.append(nb)

def is_valid_neighbor(nb, visited, rooms) -> bool:
    row, col = nb
    return row >= 0 and row < len(rooms) and col >= 0 and col < len(rooms[0]) and rooms[row][col] != -1 and (nb not in rooms)
    
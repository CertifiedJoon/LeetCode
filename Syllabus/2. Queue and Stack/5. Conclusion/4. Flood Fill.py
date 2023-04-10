from typing import List
from collections import deque

def floodFill(image: List[List [int]], sr: int, sc: int, color: int) -> None:
  match = image[sr][sc]
  q = deque()
  q.append((sr, sc))
  while q:
    r, c = q.popleft()
    image[r][c] = color
    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for nb in neighbors:
      if isValid(nb, image, match):
        q.append(nb)

def isValid(nb, image, match):
  r = nb[0]
  c = nb[1]
  return r >= 0 and r < len(image) and c >= 0 and c < len(image[0]) and image[r][c] == match

image =  [[1,1,1],[1,1,0],[1,0,1]]
floodFill(image, 1, 1, 2)

for row in image:
  print(row)
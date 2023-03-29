from math import floor, sqrt
from collections import deque

def perfect_squares(n: int) -> int:
  q = deque()
  q.append([n, 0])
  while q:
    num, length = q.popleft()
    if num == 0: return length
    for i in range(floor(sqrt(num)), -1, -1):
      q.append([num - i * i, length + 1])

print(perfect_squares(13))
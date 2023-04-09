from collections import deque
class StackQueue:
  def __init__(self):
    self._queue = deque()
  
  def push(self, val: int) -> None:
    self._queue.append(val)

  def pop(self) -> int:
    for _ in range(len(self._queue) - 1):
      self._queue.append(self._queue.popleft())
    return self._queue.pop()

  def empty(self) -> bool:
    return len(self._queue) == 0
class MinStack:
  def __init__(self):
    self._min_stack = [] # [(latestMin, count)] works as a timestamp
    self._stack = []

  def push(self, val: int) -> None:
    self._stack.append(val)
    if not self._min_stack or val < self._min_stack[-1][0]:
      self._min_stack((val, 1))
    elif val == self._min_stack[-1][0]:
      self._min_stack[-1][1] += 1
  
  def pop(self) -> int:
    popped = self._stack.pop()
    if popped == self._min_stack[-1][0]:
      self._min_stack[-1][1] -= 1
    if self._min_stack[-1][1] == 0:
      self._min_stack.pop()
    return popped
  
  def top(self) -> int:
    return self._stack[-1]
  
  def getMin(self) -> int:
    return self._min_stack[-1][0]
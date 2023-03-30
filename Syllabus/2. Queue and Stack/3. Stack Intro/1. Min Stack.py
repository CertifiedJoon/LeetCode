class MinStack:
  def __init__(self):
    """
    _minStack => work similar to timestamp record minimum at given point in stack
    , stores [min, count]
    _stack => conventional stack
    """
    _minStack = []
    _stack = []

  def push(self, val: int):
    self._stack.append(val)
    if len(self._minStack) == 0 or self._minStack[-1][0] >= val:
      if val == self._minStack[-1][0]:
        self._minStack[-1][1] += 1
      else:
        self._minStack.append([val, 1])
  
  def pop(self):
    ret = self._stack.pop()
    if ret == self._minStack[-1][0]:
      if self._minStack[-1][1] == 1:
        self._minStack.pop()
      else:
        self._minStact[-1][1] -= 1
    return ret


  def top(self):
    return self._stack[-1]
  
  def getMin(self):
    return self._minStack[-1][0]
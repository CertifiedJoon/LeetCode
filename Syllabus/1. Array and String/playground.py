class StackQueue:
  def __init__(self):
    self._pop_stack = []
    self._push_stack = []

  def push(self, val: int) -> None:
    self._push_stack.append(val)
  
  def pop(self) -> int:
    if not self._pop_stack:
      while self._push_stack:
        self._pop_stack.append(self._push_stack.pop())
    return self._pop_stack.pop()

  def peek(self) -> int:
    if not self._pop_stack:
      while self._push_stack:
        self._pop_stack.append(self._push_stack.pop())
    return self._pop_stack[-1]
  
  def empty(self) -> bool:
    return not (self._pop_stack and self._push_stack)

class QueueByStack:
  """
    Implication is that we must try to save f(n) time to accomodate an expensive
    operation that takes O(f(n)) time and happens every f(n) iteration
  """
  def __init__(self):
    self._stack_push = []
    self._stack_pop = []

  def empty(self) -> bool:
    return not self._stack_push and not self._stack_pop
  
  def push(self, val : int):
    self._stack_push.append(val)
  
  def pop(self) -> int:
    if not self._stack_pop:
      while self._stack_push:
        self._stack_pop.append(self._stack_push.pop())
    return self._stack_pop.pop()
  
  def peek(self) -> int:
    if not self._stack_pop:
      while self._stack_push:
        self._stack_pop.append(self._stack_push.pop())
    return self._stack_pop[-1]
  
qs = QueueByStack()
for i in range(10):
  qs.push(i)
for j in range(10):
  print(qs.pop())
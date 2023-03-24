class MovingAverage:
  def __init__(self, size: int):
    self._window = [0 for _ in range(size)]
    self._start = 0
    self._end = size - 1
    self._curr_size = 0
    self._current_sum = 0

  def next(self, value:int) -> float:
    left = self._start
    right = self._end
    size = len(self._window)
    self._current_sum -= self._window[left]
    self._start = (left + 1) % size
    self._end = (right + 1) % size
    self._window[self._end] = value
    self._current_sum += value
    self._curr_size = min(self._curr_size + 1, size)
    return (self._current_sum) / self._curr_size
  
movAvr = MovingAverage(3)

print(movAvr.next(1))
print(movAvr.next(2))
print(movAvr.next(3))
print(movAvr.next(4))
print(movAvr.next(5))
class TwoSum:
  def __init__(self):
    self.numbers = set()
  
  def add(self, number: int) -> None:
    self.numbers.add(number)
  
  def find(self, value: int) -> bool:
    for number in self.numbers:
      if value - number in self._numbers and number != value - number:
        return True
    return False
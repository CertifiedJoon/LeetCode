class Logger:
  def __init__(self):
    self._last_printed = dict() # msg: timestamp
  
  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if message in self._last_printed and self._last_printed[message] - timestamp < 10:
      return False
    self._last_printed[message] = timestamp
    return True
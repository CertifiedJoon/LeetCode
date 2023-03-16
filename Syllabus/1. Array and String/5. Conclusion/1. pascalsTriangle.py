from typing import List


def pascalsTriangle(rowIndex: int) -> List[int]:
  ret = [1]
  if rowIndex == 0:
    return ret
  
  for i in range(0, rowIndex):
    ret.append(ret[-1] * (rowIndex - i) // (i + 1))
  return ret

print(pascalsTriangle(4))
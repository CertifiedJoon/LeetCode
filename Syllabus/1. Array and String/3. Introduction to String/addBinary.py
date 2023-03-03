class Solution:
  def addBinary(self, a: str, b: str):
    i = len(a) - 1
    j = len(b) - 1
    carry = False
    result = ["" for _ in range(max(i,j) + 2)]
    while (i >= 0 or j >= 0):
      if i >= 0 and j >= 0:
        result[i + 1], carry = self.add(carry, a[i], b[j])
        i -= 1
        j -= 1
      elif i >= 0:
        result[i + 1], carry = self.add(carry, a[i])
        i -= 1
      else:
        result[j + 1], carry = self.add(carry, b[j])
        j -= 1
    if carry:
      result[0] = "1"
    return "".join(result)
  
  def add(self, carry: bool, first_digit: str, second_digit: str = None):
    if not second_digit:
      second_digit = "0"
    
    result = ""
    if carry:
      if first_digit == "1" and second_digit == "1":
        result = "1"
      elif first_digit == "1" or second_digit == "1":
        result = "0"
      else:
        result = "1"
        carry = False
    else:
      if first_digit == "1" and second_digit == "1":
        result = "0"
        carry = True
      elif first_digit == "1" or second_digit == "1":
        result = "1"
      else:
        result = "0"

    return result, carry

print(Solution().addBinary("11", "1"))
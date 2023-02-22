class Solution:
  def plusOne(self, digits):
    number = 0
    for digit in digits:
      number = number * 10 + digit
    number += 1

    ret = []
    while (number > 0):
      ret.append(number % 10)
      number = number // 10
    return reversed(ret)
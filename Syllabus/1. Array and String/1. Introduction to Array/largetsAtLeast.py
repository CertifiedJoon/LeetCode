class Solution:
  def largestAtLeast(self, nums):
    largest = second_largest = -1
    for num in nums:
      if num >= second_largest * 2 and num >= largest * 2:
        largest = num
        second_largest = round(largest / 2)
      elif num > second_largest:
        if num * 2 > largest:
          largest = -1
        second_largest = num
    return largest
class Solution:
  def pivotIndex(self, nums):
    total = sum(nums)
    current_sum = 0
    for i in range(len(nums)):
      if current_sum == total - nums[i] - current_sum:
        return i
      current_sum += nums[i]
    return -1

def max_consecutive_ones(nums: List[int]) -> int:
  slow = fast = 0
  max_len = 0
  while fast < len(nums):
    while (slow < len(nums) and nums[slow] == 0): slow += 1
    fast = slow
    while (fast < len(nums) and nums[fast] == fast): fast += 1
    if (fast - slow) > max_len:
      max_len = fast - slow
    slow = fast
  return max_len
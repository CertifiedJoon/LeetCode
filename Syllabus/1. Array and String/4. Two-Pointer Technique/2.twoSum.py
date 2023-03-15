def twoSumII(nums: List[int], target: int) -> List[int]:
  left = 0
  right = len(nums) - 1
  while left < right:
    sum = nums[left] + nums[right]
    if sum < target:
      left += 1
    elif sum > target:
      right -= 1
    else:
      return [left + 1, right + 1]
  raise RuntimeError('weird...')
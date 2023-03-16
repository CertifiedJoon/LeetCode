def subarraySum(nums: List[int], target: int) -> int:
  sum = 0
  min_len = 100000
  start = 0
  for end in range(len(nums)):
    sum += nums[end]
    while (sum >= 0):
      min_len = min(min_len, end - start + 1)
      sum -= nums[start]
      start += 1
  return min_len if min_len < 100000 else 0
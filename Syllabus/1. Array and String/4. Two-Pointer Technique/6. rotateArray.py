def rotateArray(nums: List[int], k: int) -> None:
  curr = 0
  v = nums[0]
  for _ in range(len(nums)):
    next = (curr + k) % len(nums)
    temp = nums[next]
    nums[next] = v
    curr = next
    v = temp
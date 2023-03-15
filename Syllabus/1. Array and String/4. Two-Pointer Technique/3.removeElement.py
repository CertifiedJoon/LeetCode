def remove_element(nums: List[int], val: int) -> None:
  swap_from = 1
  swap_to = 0
  while swap_from < len(nums):
    while (swap_to < len(nums) and nums[swap_to] != val): swap_to += 1
    swap_from = swap_to + 1
    while (swap_from < len(nums) and nums[swap_from] == val): swap_from += 1
    if (swap_from < len(nums)):
      temp = nums[swap_from]
      nums[swap_from] = nums[swap_to]
      nums[swap_to] = temp
  return 0
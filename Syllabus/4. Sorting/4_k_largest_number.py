def k_largest(nums, k):
  lo = 0
  hi = len(nums) - 1
  i = 0
  

  while i < hi:
    if nums[i] == 0:
      nums[i], nums[lo] = nums[lo], nums[i]
      lo += 1
      i += 1
    elif nums[i] == 2:
      nums[i], nums[hi] = nums[hi], nums[i]
      hi -= 1
    else:
      i += 1
    
  if lo > len(nums) - k:
    k_largest(nums[:lo], lo - k)
  elif hi < len(nums) - k:
    k_largest(nums[hi:], k - hi)
  else:
    return nums[i]
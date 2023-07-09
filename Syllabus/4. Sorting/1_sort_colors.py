def sort_colors(nums):
  red_index = 0
  blue_index = len(nums) - 1
  i = 0
  
  while i < blue_index:
    if nums[i] == 0:
      nums[i], nums[red_index] = nums[red_index], nums[i]
      red_index += 1
      i += 1
    elif nums[i] == 2:
      nums[i], nums[blue_index] = nums[blue_index], nums[i]
      blue_index -= 1
    else:
      i += 1
  
  return nums
def two_sum(nums, target):
  remainder_index = {} # target - num : index
  for i in range(len(nums)):
    if nums[i] in remainder_index:
      return [remainder_index[nums[i]], i]
    remainder_index[target - nums[i]] = i
  return -1

print(two_sum([3,2,4,5], 6))
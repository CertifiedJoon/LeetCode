def removeDuplicates(nums):
  insert = next = 0
  prev = nums[0]
  while next < len(nums):
    while next < len(nums) and nums[next] == prev: 
      next += 1
    nums[insert] = nums[next -1]
    prev = nums[min(next, len(nums) - 1)]
    insert += 1
  return insert

nums = [0,0,1,2,2,2,3,3,3,4]
print(nums[:removeDuplicates(nums)])
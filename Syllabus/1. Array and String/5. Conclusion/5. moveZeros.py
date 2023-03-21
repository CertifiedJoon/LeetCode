def moveZeroes(nums):
  insert = 0
  while nums[insert] != 0:
    insert += 1
  next = insert
  
  while next < len(nums):
    while next < len(nums) and nums[next] == 0: next += 1
    if next != len(nums):
      temp = nums[next]
      nums[next] = nums[insert]
      nums[insert] = temp
      insert += 1
      while insert <= next and nums[insert] != 0: insert += 1

nums = [0,1,0,1,0,3,0,0,0,12,0]
moveZeroes(nums)
print(nums)
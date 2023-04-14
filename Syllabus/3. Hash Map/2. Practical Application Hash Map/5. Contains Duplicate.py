from typing import List

def containsDuplicateK(nums: List[int], k: int) -> bool:
  last_seen = dict()
  for i in range(len(nums)):
    if nums[i] in last_seen:
      if i - last_seen[nums[i]] <= k:
        return True
    last_seen[nums[i]] = i
  return False

print(containsDuplicateK([1,2,3,1,2,3], 2))
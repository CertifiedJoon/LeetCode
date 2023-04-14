from typing import List

def intersectionII(nums1: List[int], nums2: List[int]) -> List[int]:
  first = dict()
  for num in nums1:
    if num not in first:
      first[num] = 0
    first[num] += 1

  ret = []
  for num in nums2:
    if num in first and first[num] > 0:
      ret.append(num)
      first[num] -= 1
  
  return ret

print(intersectionII([1,2,2,1],[2,2]))
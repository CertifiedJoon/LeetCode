def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
  result = []
  set_nums1 = set(nums1)
  for num in nums2:
    if num in set_nums1:
      result.append(num)
  return num
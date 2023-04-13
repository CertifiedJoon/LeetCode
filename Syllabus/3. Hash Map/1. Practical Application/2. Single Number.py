def single_number(nums):
  uniq = set()
  for num in nums:
    if num in uniq:
      uniq.remove(num)
    else:
      uniq.add(num)
  for a in uniq:
    return a
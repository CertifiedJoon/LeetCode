def containsDuplicate(self, nums):
  uniq = set()
  for num in nums:
    if num in uniq:
      return True
    uniq.add(num)
  return False
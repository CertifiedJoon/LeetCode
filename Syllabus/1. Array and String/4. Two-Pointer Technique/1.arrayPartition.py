def arrayPartition(nums: List[int]) -> int:
  nums.sort()
  sum = 0
  for i in range(len(nums) // 2):
    sum += nums[i * 2]
  return sum

def arrayPartitionCountSort(nums: List[int]) -> int:
  bucket = [0 for _ in range(len(nums) //2)]
  sum = 0
  for num in nums:
    bucket[num + len(nums) // 2] += 1
  isEvenIndex = True
  for i in range(len(bucket)):
    while bucket[i]:
      if isEvenIndex:
        sum += i - len(nums) // 2
      bucket[i] -= 1
      isEvenIndex = not isEvenIndex
  return sum
def findTargetSumWays(nums: List[int], target:int) -> int:
  expr_stck = [(nums[0], 0), (-nums[0], 0)]
  counter = 0
  while expr_stck:
    expr, i = expr_stck.pop()
    if i == len(nums) - 1:
      if  expr == target:
        counter += 1
    else:
      expr_stck.append((expr + nums[i + 1], i + 1))
      expr_stck.append((expr - nums[i + 1], i + 1))
  return counter

def findTargetSumWays2(nums, target):
  total = nums.sum()
  dp = [0 for _ in range(2 * total + 1)] # shift to allow negative integers to fit in dp array
  dp[total - nums[0]] += 1
  dp[total + nums[0]] += 1
  for i in range(len(nums)):
    new_dp = [0 for _ in range(2 * total + 1)]
    for sum in range(-total, total + 1):
      new_dp[sum + total + nums[i]] += dp[sum + total]
      new_dp[sum + total - nums[i]] += dp[sum + total]
    dp = new_dp
  return dp[target + total]
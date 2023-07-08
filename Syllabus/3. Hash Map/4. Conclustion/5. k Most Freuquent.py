from collections import defaultdict

def k_most_fequent(nums, k):
  major_league = defaultdict(int)
  minor_league = defaultdict(int)

  for num in nums:
    if len(major_league) < k:
      major_league[num] += 1
    else: 
      if num in major_league:
        major_league[num] += 1
      else:
        minor_league[num] += 1
      
from collections import Counter

def jewels_and_stones(jewels, stones):
  counter = Counter(stones)
  return sum(counter[jewel] for jewel in jewels)


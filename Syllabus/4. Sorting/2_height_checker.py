def height_checker(heights):
  expected = sorted(heights)
  
  cnt = 0
  for x, y in zip(expected, heights):
    if x != y:
      cnt += 1
  return cnt
def isomorphicStrings(strs):
  transformationSet = set()
  #First transform characters by the index first seen
  for str in strs:
    transformed = [0 for _ in range(len(str))]
    first_seen = {}
    for i, c in enumerate(str):
      if c not in first_seen:
        first_seen[c] = i
      transformed[i] = first_seen[c]
      transformationSet.add(transformed)
  return len(transformationSet) == 1
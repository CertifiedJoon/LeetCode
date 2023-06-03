from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
  groups = dict()
  for s in strs:
    transform = []
    first_seen = dict()
    for i, c in enumerate(s):
      if c not in first_seen:
        first_seen[c] = i
      transform.append(str(first_seen[c]))

    key = "".join(transform)
    print(key)
    if key not in groups:
      groups[key] = [s]
    else:
      groups[key].append(s)
  
  return [_ for _ in groups.values()]

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
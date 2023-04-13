def is_isomorphic(s: str, t: str) -> bool:
  char_mapping = dict()
  i = 0
  for a, b in zip(s,t) : # assuming that length of s and t are always equal
    if a in char_mapping:
      if char_mapping[a] != b:
        return False
    else:
      char_mapping[a] = b
  return True

print(is_isomorphic('egg', 'acd'))
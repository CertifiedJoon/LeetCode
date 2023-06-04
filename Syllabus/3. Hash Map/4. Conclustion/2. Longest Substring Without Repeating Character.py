def longest_uniq_subtring(s: str) -> int:
  find = dict() # can be optimized with plain array, since just alnum
  longest_len = 0
  curr_len = 0
  for i, c in enumerate(s):
    if c not in find:
      find[c] = i
      curr_len += 1
    else:
      curr_len = i - find[c]
      find[c] = i

    if curr_len > longest_len:
      longest_len = curr_len

    return longest_len
    
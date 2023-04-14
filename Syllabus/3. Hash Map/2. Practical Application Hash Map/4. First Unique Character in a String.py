def first_unique_char(s: str) -> int:
  counter = dict()
  for c in s:
    if c not in counter:
      counter[c] = 0
    counter[c] += 1
  
  for i in range(len(s)):
    if counter[s[i]] == 1:
      return i
  
  return -1

print(first_unique_char('loveleetcode'))
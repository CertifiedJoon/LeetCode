def group_shifted_strings(strs):
  groups = dict()
  for s in strs:
    transform = []
    for i in range(1, len(s)):
      transform.append(str(abs(ord(s[i]) - ord(s[i -1])) % 24))
    key = "".join(transform)
    if key not in groups:
      groups[key] = [s]
    else:
      groups[key].append(s)

  return [_ for _ in groups.values()]

print(group_shifted_strings(["abc","bcd","acef","xyz","az","ba","a","z"]))
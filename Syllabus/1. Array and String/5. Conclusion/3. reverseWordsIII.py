def reverseWordsIII(s):
  words = []
  i = 0
  while i < len(s):
    while i < len(s) and s[i] == ' ': i += 1
    start = i
    while i < len(s) and s[i] != ' ': i += 1
    if i != start:
      words.append(s[i - 1 : start - 1 if start > 0 else None : -1])
  return ' '.join(words)

print(reverseWordsIII("Sky is Blue Boiz"))

def reverseWords(s):
  word_stck = []
  i = 0
  while i < len(s):
    while i < len(s) and s[i] == ' ': i += 1
    start = i
    while i < len(s) and s[i] != ' ': i += 1
    if i != start:
      word_stck.append(s[start: i])
  return ' '.join(word_stck[::-1])

print(reverseWords("   Sky is Blue Boiz"))

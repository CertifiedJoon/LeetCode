class Solution:
  def strStr(self, haystack: str, needle: str):
    m = len(haystack)
    n = len(needle)
    i = j = 0
    lps = self.lpsCalc(needle, n)

    if not n:
      return ""
    
    while i < m:
      print(j)
      if haystack[i] == needle[j]:
        i += 1
        j += 1
      if (j == n):
        return i - n
      if (i < m) and haystack[i] != needle[j]:
        if (j):
          j = lps[j - 1]
        else:
          i += 1
    
    return -1

  def lpsCalc(self, needle: str, n: int):
    lps = [0 for _ in range(n)]
    len = 0
    i = 1
    while i < n:
      if needle[len] == needle[i]:
        len += 1
        lps[i] = len
        i += 1
      elif len:
        len = lps[len - 1]
      else:
        i += 1
    return lps
  
print(Solution().strStr("racetrack", "rack"))
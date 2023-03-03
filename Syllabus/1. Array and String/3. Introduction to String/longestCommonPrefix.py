class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
      return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
      j = 0
      while (j < len(strs[i]) and prefix[j] == strs[i][j]):
        j += 1
      if j == 0:
        return ""
      prefix = prefix[:j]
    return prefix

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
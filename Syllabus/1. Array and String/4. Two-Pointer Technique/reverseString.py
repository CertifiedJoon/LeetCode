class Solution:
  def reverseString(self, s: list[str]) -> None:
    """In place reverse"""
    i = 0
    j = len(s) - 1
    while i < j:
      i, j = self.swap(s, i, j)
    
  def swap(self, s: list[str], i: int, j: int):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    return i + 1, j - 1
    
s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
print(s)
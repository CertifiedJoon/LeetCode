class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.longestFromCentre(s,i,i), self.longestFromCentre
            (s,i,i+1), res, key=len)
        return res       
        
    def longestFromCentre(self,s,l,r):
        while 0<=l and r < len(s) and s[l]==s[r]:
            l-=1; r+=1
        return s[l+1:r]

sl = Solution()
print(sl.longestPalindrome("babadda"))
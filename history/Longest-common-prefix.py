import pysnooper
class Solution(object):
    @pysnooper.snoop()
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for str in strs:
            for i in range(min(len(prefix),len(str))):
                if prefix[i] != str[i]:
                    prefix = prefix[:i]
                    break
        return prefix

sl = Solution()
sl.longestCommonPrefix(["flower","flow","flight"])

class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        i = len(s) - 1
        while(s[i] == " " and i >= 0):
            i -= 1
            print(i)
        while(s[i] != " " and i >= 0):
            count += 1
            i -= 1
        return count;

sl = Solution()
print(sl.lengthOfLastWord("hello world"))

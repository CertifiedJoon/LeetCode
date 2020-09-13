class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            return (True if str(x) == str(x)[::-1] else False)

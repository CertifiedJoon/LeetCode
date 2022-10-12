class Solution(object):
    def longestPalindrome(self, s):
        counter = {}
        tolerance = True
        l = 0
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for key, val in counter.items():
            if val > 1:
                l += (val // 2) * 2
                if val % 2 != 0 and tolerance:
                    l += 1
                    tolerance = False
            elif tolerance:
                l += 1
                tolerance = False
        return l


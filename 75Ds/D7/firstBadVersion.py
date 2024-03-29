# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left <= right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left
            
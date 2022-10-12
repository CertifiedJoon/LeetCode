class Solution:
    def mySqrt (self, x):
        return self.bsearch(x,0,x)
    
    def bsearch(self, x, left, right):
        mid = (left + right) // 2

        if (pow(mid, 2) == x or ((pow(mid + 1, 2) > x) and pow(mid, 2) < x)):
            return mid

        elif (mid * mid < x):
            return self.bsearch(x, mid + 1, right)

        else:
            return self.bsearch(x, left, mid - 1)
    

sl = Solution()
print(sl.mySqrt(9))
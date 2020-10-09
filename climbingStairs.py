class Solution:
    def climbStairs(self, n):
        prev = fibo = 1
        i = 1

        while(i < n):
            temp = fibo
            fibo += prev
            prev = temp
            i += 1

        return fibo

sl = Solution()
print(sl.climbStairs(6))
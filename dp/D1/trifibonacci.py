class Solution(object):
    def tribonacci(self, n):
        if n < 2:
            return n
        if n == 2:
            return 1
        fib = 0
        a = 0; b = 1; c = 1
        for i in range(3, n + 1):
            fib = a + b + c
            a = b
            b = c
            c = fib
        return fib
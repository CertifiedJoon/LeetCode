from math import sqrt


def rec_fib(n):
    """
    Recursion
    T : O(2^n)
    S : O(n)
    """
    if n < 2:
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)

def memo_fib(n):
    """
    Memoization
    T : O(n)
    S : O(n)
    """
    if n < 2:
        return n
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

def bottom_up_dp_fib(n):
    """
    Bottom Up Dp 
    T : O(n)
    S : O(1)
    """
    if n < 2:
        return n
    a = 0; b = 1; c = 0
    for _ in range(0, n):
        c = a + b
        a = b
        b = c
    return c

def phi_fib(n):
    """
    Binet's Nth-term approximation
    T : O(1)
    S : O(1)
    works for small n
    """
    phi = (sqrt(5) + 1) / 2
    return round(pow(phi, n) / sqrt(5))

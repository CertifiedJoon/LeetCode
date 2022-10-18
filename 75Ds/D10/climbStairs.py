def climbStairs(n):
    if n < 4:
        return n
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3
    for i in range(4, n + 1):
        memo[i] = memo[i -1] + memo[i - 2]
    
    return memo[n]

print(climbStairs(44))
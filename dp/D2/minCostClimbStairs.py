def minCostClimbingStairs(cost):
    return optimized_dp_helper(cost)

def rec_helper(cost, curr):
    if curr >= len(cost):
        return 0
    return (cost[curr] if curr > -1 else 0) + min(rec_helper(cost, curr + 1), rec_helper(cost, curr + 2))

def dp_helper(cost):
    if len(cost) == 2:
        return min(cost[0], cost[1])
    n = len(cost)
    min_cost_memo = [0] * n
    min_cost_memo[n - 1] = cost[n - 1]
    min_cost_memo[n - 2] = cost[n - 2]
    curr = len(cost) - 3
    while curr >= 0:
        min_cost_memo[curr] = cost[curr] + min(min_cost_memo[curr + 1], min_cost_memo[curr + 2])
        curr -= 1
    return min(min_cost_memo[0], min_cost_memo[1])

def optimized_dp_helper(cost):
    if len(cost) == 2:
        return min(cost[0], cost[1])
    n = len(cost)
    first = cost[-1]
    second = cost[-2]
    total = 0
    curr = len(cost) - 3
    while curr >= 0:
        total = cost[curr] + min(first, second)
        first = second
        second = total 
        curr -= 1
    return min(first, second)

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
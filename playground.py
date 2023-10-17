"""
Premise:
1. given daily temperature (list of int) return an array answer such that answer [i]
is the number of days until warmer.

Constraints:
1. 30 < temperatures[i] <= 100

Plausible solutions:
1. brute force X
2. monotonic stack approach (O(n))
3. top down approach (saves space at the expense of some runtime) (should be considered
depending on the statistical distribution of the temperature)

Logic:
1. maintain monotonic stack 
2. compare head of the stack with the current ith element
"""

from typing import *


def daily_temperatures(temperatures: List[int]):
    res = [0 for _ in range(len(temperatures))]
    days_waiting_for_warmer_day = [(temperatures[0], 0)]

    for i, temp in enumerate(temperatures):
        while days_waiting_for_warmer_day and days_waiting_for_warmer_day[-1][0] < temp:
            _, pop_i = days_waiting_for_warmer_day.pop()
            res[pop_i] = i - pop_i
        days_waiting_for_warmer_day.append((temp, i))

    return res


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))

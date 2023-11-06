"""
Premise:
1. given integer, return the least number of perfect square numbers that sum to n.

Constaints:
1. 1 <= n <= 10^4

first level
12 -> [1, 4, 9] 

second level
11 -> [1, 4, 9]
8 -> [1, 4]
3 -> [1]

"""

import math


def squareSum(n: int):
    # queue implemented in set to reduce redundancy
    queue = set()
    queue.add(n)

    level = 0

    while queue:
        newQueue = set()
        for elem in queue:
            if elem == 0:
                return level
            for root in range(1, math.sqrt(elem)):
                if elem - root**2 > 0:
                    newQueue.add(elem - root**2)
        queue = newQueue
        level += 1

    raise RuntimeError("Error Square sum impossible.")

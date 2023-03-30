import copy
from math import floor, sqrt
from collections import defaultdict, deque
import random
import time
import unittest

def perfect_squares(n: int) -> int:
  q = deque()
  q.append([n, 0])
  while q:
    num, length = q.popleft()
    if num == 0: return length
    for i in range(floor(sqrt(num)), -1, -1):
      q.append([num - i * i, length + 1])


def numSquares(n):

    # list of square numbers that are less than `n`
    square_nums = [i * i for i in range(1, int(n**0.5)+1)]

    level = 0
    queue = {n}
    while queue:
        level += 1
        #! Important: use set() instead of list() to eliminate the redundancy,
        # which would even provide a 5-times speedup, 200ms vs. 1000ms.
        next_queue = set()
        # construct the queue for the next level
        for remainder in queue:
            for square_num in square_nums:    
                if remainder == square_num:
                    return level  # find the node!
                elif remainder < square_num:
                    break
                else:
                    next_queue.add(remainder - square_num)
        queue = next_queue
    return level

class Test(unittest.TestCase):
    test_cases = [[8, 2], [636, 4], [778, 2], [1156, 1], [694, 3], [1257, 3], [1987, 3], [1773, 2], [757, 2], [829, 2], [1386, 3], [665, 3], [1144, 3], [1418, 2], [441, 1], [1669, 2], [1730, 2], [648, 2], [325, 2], [1748, 3], [1355, 3], [513, 3], [830, 3], [1606, 3], [1365, 3], [82, 2], [1637, 2], [1047, 4], [892, 4], [1859, 3], [987, 3], [1470, 3], [1815, 4], [1909, 3], [89, 2], [1183, 4], [106, 2], [760, 3], [245, 2], [1035, 3]]
    test_functions = [
        perfect_squares,
        numSquares
    ]
    def test_sort(self):        
        num_runs = 10
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for case, expected in self.test_cases:
                for squares in self.test_functions:
                    start = time.process_time()
                    assert(
                        squares(case) == expected
                    ), f"{squares.__name__} failed at {case}"
                    function_runtimes[squares.__name__] += (
                        time.process_time() - start
                    ) * 1000
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()
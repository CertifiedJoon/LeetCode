import unittest
import time
import random
from collections import defaultdict
import copy

def is_sorted(nums):
    prev = -1
    for n in nums:
        if n < prev:
            return False
        prev = n 
    return True

def is_sorted_monte_carlo(nums):
    for _ in range(100):
        i, j = random.choices(range(len(nums)), k = 2)
        i, j = max(i,j), min(i,j)
        if nums[i] < nums[j]:
            return False
    return True


class Test(unittest.TestCase):
    test_cases = []
    test_functions = [
        is_sorted,
        is_sorted_monte_carlo
    ]
    def test_sort(self):
        for _ in range(40):
            arr = random.choices(range(20000), k = 20000)
            sorted_arr = sorted(arr)
            self.test_cases.append((arr, False))
            self.test_cases.append((sorted_arr, True))
        
        num_runs = 10
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for arr, expected in self.test_cases:
                copied = copy.deepcopy(arr)
                for is_sort in self.test_functions:
                    start = time.process_time()
                    answer = is_sort(copied)
                    assert(
                        answer == expected
                    ), f"{is_sort.__name__} failed at {arr}"
                    function_runtimes[is_sort.__name__] += (
                        time.process_time() - start
                    ) * 1000
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()
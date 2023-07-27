from collections import Counter


def delete_and_ear(nums):
    """
    Premise
    1. Given an integer array nums.
    2. Maximize the number of points you get
    3. pick nums[i] and earn nums[i]
    4. delete nums[i] - 1 and nums[i] + 1

    Constraints
    1. 1 <= nums.length <= 20000
    2. 1 <= nums[i] <= 10000


    Logic
    1.  First Thought => delete operation, if it is done in coventional way
        will be costly
    2.  Now conceptualize a sorted version -> then it is equal to deleting its next smaller
        next bigger values.
    3.  So, Create a counter. O(N)
    4.  Use the counter.keys to iterate and DP O(N)
    """

    nums_counter = Counter(nums)
    max_number = max(list(nums_counter))

    def get_points(num):
        return num * nums_counter[num]

    dp_first = 0
    dp_second = get_points(1)

    for num in range(2, max_number + 1):
        dp_first, dp_second = dp_second, max(dp_second, dp_first + get_points(num))

    return dp_second

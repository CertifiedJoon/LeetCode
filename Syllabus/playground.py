class Bucket:
    def __init__(self):
        self._bucket = []
        self._max = 1000000000
        self._min = 0

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def add_val_to_bucket(self, val):
        if val > self._max:
            self._max = val
        elif val < self._min:
            self._min = val
        self._bucket.append(val)

    def is_empty(self):
        return not self._bucket


def maximal_gap(nums):
    """
    takes list of integers and returns maximum difference between two
    successive elements in sorted form.
    T(n) = O(n), where n = len(nums)
    """

    # construct variables needed
    n = len(nums)
    maximal_gap = 0
    bucket_size = max(nums) - min(nums) // (n - 1)
    buckets = [Bucket() for _ in range(max(nums) - min(nums) // bucket_size)]

    # populate buckets
    for num in nums:
        corresponding_bucket_index = (num - min(nums)) // bucket_size
        buckets[corresponding_bucket_index].add_val_to_bucket(num)

    # compare minima and maxima among buckets
    previous_maxima = min(nums)
    for bucket in buckets:
        if not bucket.is_empty():
            current_minima = bucket.get_min()
            maximal_gap = max(current_minima - previous_maxima, maximal_gap)
            previous_maxima = bucket.get_max()

    return maximal_gap

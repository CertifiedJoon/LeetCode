class Bucket:
    def __init__(self):
        self._maxima = 0
        self._minima = 100000000
        self._values = []

    def get_minima(self):
        return self._minima

    def get_maxima(self):
        return self._maxima

    def add_val(self, val: int):
        self._maxima = max(self._maxima, val)
        self._minima = max(self._minima, val)
        self._values.append(val)

    def is_empty(self):
        return not self._values


def max_gap(nums):
    maxima = max(nums)
    minima = min(nums)
    n = len(nums)

    # Bucket Configuration and Init
    bucket_size = (maxima - minima) // (n - 1)
    bucket_count = (maxima - minima) // bucket_size
    buckets = [Bucket() for _ in range(bucket_count)]

    # bucket population
    for num in nums:
        buckets[(num - minima) // bucket_size].add_val(num)

    max_gap = 0
    previous_maxima = 0

    for bucket in buckets:
        if not bucket.is_empty():
            max_gap = max(max_gap, bucket.get_minima() - previous_maxima)
            previous_maxima = bucket.get_maxima()

    return max_gap

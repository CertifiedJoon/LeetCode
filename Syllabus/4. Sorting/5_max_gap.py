class Bucket:
    def __init__(self):
        self._maxima = 0
        self._minima = 1000000
        self._values = []

    def add_value(self, value):
        if value > self._maxima:
            self._maxima = value
        elif value < self._minima:
            self._minima = value

        self._values.append(value)

        return

    def get_maxima(self):
        return self._maxima

    def get_minima(self):
        return self._minima


def max_gap(nums):
    maxima, minima = max(nums), min(nums)
    n = len(nums)
    b = (maxima - minima) // (n - 1)
    k = (maxima - minima) // b
    buckets = [Bucket() for _ in range(k)]

    for num in nums:
        buckets[num // b].add_value(num)

    previous_bucket_maxima = buckets[0].get_maxima()
    maximal_gap = 0

    for bucket in buckets:
        if bucket.get_minima() - previous_bucket_maxima > maximal_gap:
            maximal_gap = bucket.get_minima() - previous_bucket_maxima
        previous_bucket_maxima = bucket.get_maxima()

    return maximal_gap

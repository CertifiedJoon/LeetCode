import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self._heap = heapq.heapify(nums)
        self._k = k

        while len(self._heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int):
        heapq.heappush(self._heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self._heap[0]


class KthLargest2:
    def __init__(self, k: int, nums: list[int]) -> None:
        self._heap = heapq.heapify([-num for num in nums])
        self._k = k

        while len(self._heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int):
        heapq.heappush(self._heap, -val)
        if len(self._heap) > self._k:
            heapq.heapop(self.heap)
        return -self._heap[0]

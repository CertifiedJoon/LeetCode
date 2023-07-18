import heapq


class Solution:
    def last_stone_weight(self, stones):
        max_heap = [-val for val in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone_1, stone_2 = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if stone_1 > stone_2:
                heapq.heapppush(max_heap, -(stone_1 - stone_2))

        return 0 if len(max_heap) == 0 else -(heapq.heappop(max_heap))

    def last_stone_weight_count(self, stones):
        maxima, minima, n = max(stones), min(stones), len(stones)
        buckets = [0 for _ in range(maxima - minima + 1)]

        for weight in stones:
            buckets[weight - minima] += 1

        x, y = 0, 0
        i = len(buckets) - 1
        last_weight = 0
        while i >= 0:
            if buckets[i] and x == 0:
                x = i + minima
                buckets[i] -= 1
            if buckets[i] and y == 0:
                y = i + minima
                buckets[i] -= 1
            if x != 0 and y != 0:
                buckets[x - y - minima] += 1
                last_weight = x - y - minima
                x, y = 0, 0

        return last_weight

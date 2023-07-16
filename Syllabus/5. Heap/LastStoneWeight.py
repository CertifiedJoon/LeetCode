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

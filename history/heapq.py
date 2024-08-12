import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negStones = [-weight for weight in stones]
        heapq.heapify(negStones)
        while len(negStones) > 1:
            heapq.heappush(
                negStones, (heapq.heappop(negStones) - heapq.heappop(negStones))
            )
        return -negStones[0]

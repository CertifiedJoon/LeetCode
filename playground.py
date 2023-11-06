from typing import List

import heapq


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        stone_one, stone_two = -heapq.heappop(stones), -heapq.heappop(stones)
        new_stone = abs(stone_one - stone_two)
        heapq.heappush(stones, -new_stone)

    return -stones[0]

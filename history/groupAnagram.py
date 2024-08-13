class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Premise:
        . given integer array, an integer k, retun the k most frequent elements in any order

        Contraint:
        . 1 <= nums.len <= 100,000
        . - 10,000 <= num <= 10000
        """
        heap = []
        counter = Counter(nums)

        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

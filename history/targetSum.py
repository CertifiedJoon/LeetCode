class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        intermediateResult = defaultdict(int)
        intermediateResult[nums[0]] += 1
        intermediateResult[-nums[0]] += 1

        for num in nums[1:]:
            nextResult = defaultdict(int)
            for x, count in intermediateResult.items():
                nextResult[x + num] += count
                nextResult[x - num] += count
            intermediateResult = nextResult
        return intermediateResult[target] if target in intermediateResult else 0

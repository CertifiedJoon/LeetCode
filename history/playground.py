class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Premise
        . given nums, retum the minimum number of jumps to reach the end.

        Constraint
        . 1 <= nums.length <= 10000
        . 0 <= num <= 10000
        """
        if len(nums) == 1:
            return 0

        jumpableTo = 0
        jumpedFrom = 0
        jumpCount = 0
        destination = len(nums) - 1

        for i, num in enumerate(nums):
            if i + nums[i] >= destination:
                return jumpCount + 1

            jumpableTo = max(jumpableTo, nums[i] + i)

            if i == jumpedFrom:
                jumpedFrom = jumpableTo
                jumpCount += 1

        return jumpCount


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Premise
        . given nums, return the max gap between two successive elements in sorted form

        Constrating
        . nums are non negative <= 10^9
        . algo must be linear time and linear space
        """
        if 2 > len(nums):
            return 0

        class Bucket:
            def __init__(self):
                self.max = -inf
                self.min = inf
                self.length = 0

            def put(self, val):
                self.max = max(val, self.max)
                self.min = min(val, self.min)
                self.length += 1

            def isEmpty(self):
                return self.length == 0

            def getGap(self):
                return self.max - self.min

        maximum = max(nums)
        minimum = min(nums)
        n = len(nums)
        bucketSize = (maximum - minimum) // n + 1
        bucketCount = (maximum - minimum) // bucketSize + 1
        buckets = [Bucket() for _ in range(bucketCount)]
        maxGap = 0
        prevMax = None

        for num in nums:
            buckets[(num - minimum) // bucketSize].put(num)

        for bucket in buckets:
            if bucket.isEmpty():
                continue

            if not prevMax:
                maxGap = max(maxGap, bucket.getGap())
            else:
                maxGap = max(maxGap, bucket.getGap(), bucket.min - prevMax)

            prevMax = bucket.max

        return maxGap

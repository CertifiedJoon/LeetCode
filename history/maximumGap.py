class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Premise
        . given nums, return the max gap between two successive elements in sorted form

        Constrating
        . nums are non negative <= 10^9
        . algo must be linear time and linear space
        """
        if len(nums) < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        bucketRange = maximum - minimum + 1
        bucketSize = max(bucketRange // len(nums), 1)
        bucketCnt = bucketRange // bucketSize + 1

        class Bucket:
            def __init__(self):
                self.max = -inf
                self.min = inf
                self.len = 0

            def isEmpty(self):
                return self.len == 0

            def put(self, val):
                if self.max < val:
                    self.max = val
                if self.min > val:
                    self.min = val
                self.len += 1

        buckets = [Bucket() for _ in range(bucketCnt)]

        for num in nums:
            buckets[(num - minimum) // bucketSize].put(num)

        maxGap = 0

        if any([bucket.isEmpty() for bucket in buckets]):
            prevBucketMax = buckets[0].max
            for bucket in buckets[1:]:
                if bucket.isEmpty():
                    continue
                maxGap = max(maxGap, bucket.min - prevBucketMax)
                prevBucketMax = bucket.max
        else:
            for bucket in buckets:
                if not bucket.isEmpty():
                    maxGap = max(maxGap, bucket.max - bucket.min)

        return maxGap

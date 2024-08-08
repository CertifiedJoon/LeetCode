class Solution:
    def maxSubArrayDivideAndConquer(self, nums: List[int]) -> int:
        """
        Premise
        . given integer array, find subarray with the largest sum.

        Constraints
        . 1 <= nums.length <= 100000
        . -10000 <= nums[i] <= 10000
        """
        if len(nums) == 1:
            return nums[0]

        def _maxArraySumStartingFrom(array: List[int], start: int, reverse=False):
            step = -1 if reverse else 1
            end = -1 if reverse else len(nums)
            maxArraySum = float("-inf")
            tempSum = 0

            for i in range(start, end, step):
                tempSum += nums[i]
                maxArraySum = max(maxArraySum, tempSum)

            return maxArraySum

        middleIndex = len(nums) // 2
        middleMaxSum = (
            _maxArraySumStartingFrom(nums, middleIndex)
            + _maxArraySumStartingFrom(nums, middleIndex, reverse=True)
            - nums[middleIndex]
        )
        leftHalfMaxSum = self.maxSubArray(nums[: min(middleIndex, len(nums))])
        rightHalfMaxSum = self.maxSubArray(nums[min(middleIndex + 1, len(nums) - 1) :])

        return max(leftHalfMaxSum, middleMaxSum, rightHalfMaxSum)

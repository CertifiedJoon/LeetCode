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

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Premise
        . given nums, return the minimum number of jumps to reach the end.

        Constraint
        . 0 <= nums[i] <= 1000
        """
        dp = [len(nums) for _ in range(len(nums))]
        dp[0] = 0

        for i, maxJump in enumerate(nums):
            for jump in range(1, maxJump + 1):
                if len(dp) <= (i + jump):
                    break
                dp[i + jump] = min(dp[i + jump], dp[i] + 1)

        return dp[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Premise
        . given nums, return the minimum number of jumps to reach the end.

        Constraint
        . 0 <= nums[i] <= 1000
        """
        i = 0
        jumpCnt = 0
        while i != len(nums) - 1:
            maxJump = nums[i]
            nextI = i
            m = 0
            for jump in range(1, maxJump + 1):
                if (i + jump) >= len(nums) - 1:
                    nextI = len(nums) - 1
                elif (jump + nums[i + jump]) > m:
                    m = jump + nums[i + jump]
                    nextI = jump + i
            jumpCnt += 1
            i = nextI

        return jumpCnt

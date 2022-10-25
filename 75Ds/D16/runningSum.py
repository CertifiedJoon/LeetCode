class Solution(object):
    def runningSum(self, nums):
        for i, n in enumerate(nums):
            if i != 0:
                nums[i] = n + nums[i-1]
        return nums
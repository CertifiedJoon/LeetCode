class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        operands = {} # maps integer to its index when first seen
        for i, n in enumerate(nums):
            if target - n in operands:
                return [operands[target-n], i]
            operands[n] = i 
        raise Exception
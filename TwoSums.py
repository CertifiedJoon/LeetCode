class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        prevMap = {} #val: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i

        return

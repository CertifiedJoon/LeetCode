class Solution:
    def twoSum(self, nums, target):
        #nums = [2,7,11,15], target = 9
        prev = {} # key: target-n, val: index
        for i, n in enumerate(nums):
            if i == 0:
                prev[target-n] = i
            else:
                if n in prev:
                    return (prev[n], i)
                else:
                    prev[target-n] = i
        raise Exception

print(Solution().twoSum([3,2,4], 6))
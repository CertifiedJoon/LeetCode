class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1
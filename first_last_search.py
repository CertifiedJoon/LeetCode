class Solution:
    def binarySearch(self, nums, target, realTarget):
        if not nums:
            return -1
        lo, hi = 0, len(nums) -1
        while (lo < hi):
            mid = (hi - lo) // 2 + lo
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1

        if nums[lo] == realTarget:
            return lo
        elif nums[min(len(nums) - 1, lo + 1)] == realTarget:
            return lo + 1
        elif nums[max(0, lo - 1)] == realTarget:
            return lo - 1
        else:
            return -1
        
    def searchRange(self, nums, target):
        l, r = self.binarySearch(nums, target - 0.5, target), self.binarySearch(nums, target + 0.5, target)
        return (l, r)
        
print(Solution().searchRange([5,7,7,8,8,10], 6))
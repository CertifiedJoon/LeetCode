class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1
        while (lo <= hi):
            mid = (hi - lo) // 2 + lo
            if target == nums[mid]:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
    
nums = [4,5,6,7,0,1,2]
target = 0

print(Solution().search(nums, target))
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        running_sum = 0
        
        for i, n in enumerate(nums):
            total -= n
            if total == running_sum:
                return i 
            running_sum += n 

        return -1
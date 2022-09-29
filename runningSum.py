def runningSum(nums):
    """
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    """

    prev = 0
    for i, n in enumerate(nums):
        nums[i] = n + prev
        prev = nums[i]
    
    return nums

print(runningSum([1,2,3,4]))
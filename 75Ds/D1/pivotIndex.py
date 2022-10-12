def pivotIndex(nums):
    """
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    """

    forward = [0] * len(nums)
    running_sum_back = 0
    
    for i, n in enumerate(nums):
        if i == 0:
            forward[i] = 0
        else:
            forward[i] += forward[i-1] + nums[i-1]

    pivot = -1
    for i in range(len(nums) - 1, -1, -1):
        if i != (len(nums) - 1):
            running_sum_back += nums[i+1]
        if running_sum_back == forward[i]:
            pivot = i
    return pivot

def pivotIndex2(nums):
    """
    Two pass algorithm. Much faster than the above stupid method
    """
    total = sum(nums)
    left_sum = 0
    for i, n in enumerate(nums):
        if total - left_sum - n == left_sum:
            return i
        left_sum += n
    return -1

print(pivotIndex2([1,7,3,6,5,6]))
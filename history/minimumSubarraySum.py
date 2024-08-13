def minimumSubarraySum(nums, target):
    minLen = 1000000
    start = 0
    total = 0
    for end in range(len(nums)):
        total += nums[end]
        while start < end:
            if target >= total - nums[start]:
                start += 1
                minLen = min(minLen, end - start)
                total -= nums[start]

        return minLen

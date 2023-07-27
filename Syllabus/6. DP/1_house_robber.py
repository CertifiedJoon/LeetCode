def house_robber(nums):
    a = nums[0]
    b = max(nums[:2])

    for num in nums[2:]:
        c = max(num + a, b)
        a = b
        b = c

    return c


print(house_robber([2, 7, 9, 3, 1]))

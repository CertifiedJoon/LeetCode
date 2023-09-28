def jump_game_II(nums):
    curr_end, curr_far = 0, 0
    jump_cnt = 0

    for i, jump in enumerate(nums):
        curr_far = max(curr_far, i + jump)

        if i == curr_end and i != len(nums) - 1:
            curr_end = curr_far
            jump_cnt += 1

    return jump_cnt


print(jump_game_II([2, 3, 1, 1, 4]))

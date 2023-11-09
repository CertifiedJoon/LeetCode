def reaching_point(sx, sy, tx, ty):
    while tx > sx and ty > sy:
        if tx < ty:
            ty %= tx
        else:
            tx %= ty
        if tx == sx and ty == sy:
            return True

    return False


print(reaching_point(1, 1, 3, 5))

def reaching_point(sx, sy, tx, ty):
    while tx > sx and ty > sx:
        if tx > ty:
            tx %= ty
        else:
            ty %= tx

        if (sx == tx) and (ty == tx):
            return True

    return False

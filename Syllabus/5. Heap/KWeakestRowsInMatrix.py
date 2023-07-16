def k_weakest_rows_in_a_matrix(mat: list[list[int]], k: int):
    x_len = len(mat[0])
    y_len = len(mat)

    for i, lst in enumerate(mat):
        lst.append(i)
    rad = 0
    while rad < x_len:
        for i in range(y_len):
            j = i
            if mat[i][rad] == 0:
                while j < y_len and mat[j][rad] == 0:
                    j += 1
                if j == y_len:
                    break
                mat[j], mat[i] = mat[i], mat[j]
        rad += 1
        print(mat)
    return [lst[-1] for lst in mat[y_len - k :]]


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]

print(k_weakest_rows_in_a_matrix(mat, 3))

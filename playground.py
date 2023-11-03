def generateParentheses(n: int):
    para = []

    if n == 0:
        return [""]

    for left in range(n):
        for left_string in generateParentheses(left):
            for right_string in generateParentheses(n - 1 - left):
                para.append("(" + left_string + ")" + right_string)

    return para


print(generateParentheses(4))

"""
Premise:
1. Given an encoded string return its decoded string.
2. encoding rule is k[encoded_string] = k * encoded string
3. there can be a recursive structure.


Constraints:
1. 1 <= s.length <= 30
2. input alwasy valid.
3. s are in the range [1, 300]
"""


# Decode k[encoded string]
def decode(encoded: str):
    # destructure the encoded string into k and string word
    k_stack = []
    word_stack = []
    result = []

    # buffer to store the current word
    word_buffer = []

    for c in encoded:
        if c.isnumeric():
            if word_buffer:
                word_stack.append("".join(word_buffer))
                word_buffer = []
            k_stack.append(c)
        elif c != "]" and c != "[":
            word_buffer.append(c)
        elif c == "]":
            word = ""
            if word_buffer:
                word = "".join(word_buffer)
            elif word_stack:
                word = word_stack.pop()

            k = k_stack.pop()

            if word_stack:
                word_stack[-1] = word_stack[-1] + k * word
            else:
                result.append(k * word)

            word_buffer = []

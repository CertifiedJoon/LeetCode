class Solution:
    def isValid(self, s):
        n = len(s)
        stack = ['_']
        match = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in match.keys():
                if stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 1
        
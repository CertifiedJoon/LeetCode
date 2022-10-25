class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stk = []
        t_stk = []
        for c in s:
            if c == '#':
                s_stk.pop() if s_stk else None
            else:
                s_stk.append(c)
        for c in t:
            if c == '#':
                t_stk.pop() if t_stk else None
            else:
                t_stk.append(c)
        return s_stk == t_stk
        
    def backspaceCompareSpaceOptimized(s, t):
        i = len(s) - 1; j = len(t) - 1
        i_backspaces = j_backspaces = 0

        while i >= 0 and j >= 0:
            if s[i] == '#':
                i_backspaces += 1
                i -= 1
            elif i_backspaces:
                i_backspaces -= 1
                i -= 1
            if t[j] == '#':
                j_backspaces += 1
                j -= 1
            elif j_backspaces:
                j_backspaces -= 1
                j -= 1

            if i > -1 and j > -1 and s[i] != '#' and t[j] != '#' and not j_backspaces and not i_backspaces:
                if s[i] != t[j]:
                    return False
                else:
                    i -= 1
                    j -= 1

            if i_backspaces < 0 or j_backspaces < 0:
                return False

        return i == -1 and j == -1
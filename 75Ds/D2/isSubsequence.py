def isSubsequence(s,t):
    i = j = 0
    while i < len(s):
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                break
            j += 1
        if j == len(t) and i < len(s):
            return False
    return True

print(isSubsequence('ace', 'abcde'))
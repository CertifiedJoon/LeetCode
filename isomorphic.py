def isIsomorphic(s, t):
    char_map = {}
    for x, y in zip(s,t):
        if x not in char_map and y not in char_map:
            char_map[x] = y
            char_map[y] = x
        elif x in char_map and y in char_map:
            if char_map[x] != y or char_map[y] != x:
                return False
        else:
            return False
    
    return True


print(isIsomorphic("paper", "title"))
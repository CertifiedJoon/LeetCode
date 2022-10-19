from collections import defaultdict
def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    indexes = []
    p_len = len(p)
    s_len = len(s)
    if p_len > s_len:
        return indexes
    char_count = defaultdict(int)

    for c in p:
        char_count[c] += 1

    for i in range(p_len - 1):
        char_count[s[i]] -= 1
    
    for i in range(-1, s_len - p_len):
        if i > -1 and s[i] in char_count:
            char_count[s[i]] += 1
        if s[i + p_len] in char_count:
            char_count[s[i + p_len]] -= 1
        if not any(char_count.values()):
            indexes.append(i + 1)
    
    return indexes
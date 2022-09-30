def isIsomorphic(s, t):
    char_map = {} # char mapping
    mapped_char = set() # set(char_map.values())
    for x, y in zip(s,t):
        if x not in char_map and y not in mapped_char:
            char_map[x] = y
            mapped_char.add(y)
        elif not (x in char_map and char_map[x] == y):
            return False
    
    return True

def isIsomorphicWords(words):
    """
    Extension to above problem.
    Same problem but with a group of strings instead of two.
    """
    #First Occurence Trasformation.
    transformed = set() # stores all transformed strings as a set
    for word in words:
        first_seen = {} # maps character to the index at which the char was seen for the first time
        occurence = [0] * len(word) # transformed version of each word
        for i, c in enumerate(word):
            if c not in first_seen:
                first_seen[c] = i
            occurence[i] = str(first_seen[c])
        transformed.add(' '.join(occurence))
    return len(transformed) <= 1

print(isIsomorphicWords([]))
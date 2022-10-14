def areIsomorphic(words):
    check = set()
    for word in words:
        transformed = [] # temporarily stores the transformed word
        first_seen = {} # maps character to index first seen
        for i, c in enumerate(word):
            if c not in first_seen:
                first_seen[c] = i
            transformed.append(first_seen[c])
        check.add(transformed)
    return len(check) <= 1
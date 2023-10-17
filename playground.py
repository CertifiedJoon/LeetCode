from typing import *

"""
Premise:
1. given list of strs. group them by anagrams. 

Contstraints:
1. all lowercase alphabets

Plausible Solutions:
1. bruteforce X
2. count char and find anagrams X
3. char counter string transformation (O)

Logic:
1. first create a counter (an array of len 26)
2. count char for each str into counter
3. string transform
4. hash
"""

from collections import defaultdict


def group_anagrams(strs: List[str]):
    anagram_map = defaultdict(list)

    for s in strs:
        counter = [0 for _ in range(26)]
        for c in s:
            counter[ord(c) - 97] += 1
        anagram_map["".join(str(i) for i in counter)].append(s)

    return [anagram_group for anagram_group in anagram_map.values()]


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

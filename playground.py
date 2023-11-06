from collections import defaultdict()
from typing import List

def songPairs(time: List[int]) -> int:
    song_counter = defaultdict(int)
    result = 0
    
    for t in time:
        result += song_counter[60 - t % 60 if t % 60 != 0 else 0]
        song_counter[t % 60] += 1
    
    return result
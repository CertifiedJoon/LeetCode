import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = collections.defaultdict(int)
        longest_len = largest_freq = 0
        for r in range(len(s)):
            frequency[s[r]] += 1
            curr_len = r - l + 1
            largest_freq = max(frequency[s[r]], largest_freq)
            if curr_len - largest_freq <= k:
                longest_len = max(longest_len, curr_len)
            else:
                frequency[s[l]] -= 1
                l += 1
        return longest_len
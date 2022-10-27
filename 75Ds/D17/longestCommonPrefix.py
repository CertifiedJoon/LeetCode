class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for word in strs:
            i = 0 
            while i < min(len(word), len(lcp)) and word[i] == lcp[i]:
                i += 1
            lcp = lcp[:i]

        return lcp
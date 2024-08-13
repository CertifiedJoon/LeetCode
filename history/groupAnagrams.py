class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Premise
        . Given an array of strings, group anagrams tgt

        Constraint
        . 1 <= strs.len <= 10000
        . 0 <= str.len <= 100
        """
        anagramGroup = defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagramGroup[tuple(count)].append(s)

        return anagramGroup.values()

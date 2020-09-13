class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        strip = ""
        for c in s:
            if c in strip:
                strip = strip[strip.find(c)+1:]
            strip += c
            if len(strip) > maximum:
                maximum = len(strip)
        return maximum

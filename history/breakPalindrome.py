class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        for i, c in enumerate(palindrome[: 1 + len(palindrome) // 2]):
            if ord(c) > ord("a"):
                if (i != len(palindrome) // 2) or (0 == len(palindrome) % 2):
                    return palindrome[:i] + "a" + palindrome[i + 1 :]

        return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)

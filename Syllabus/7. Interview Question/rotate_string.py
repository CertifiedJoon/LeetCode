class Solution:
    def kmp(self, A, B):
        i, j = 0, 0
        lps = self.lps(B)
        while i < len(A):
            if A[i] == B[j]:
                i += 1
                j += 1

            if j == len(B):
                return i - j

            if A[i] != B[j] and i < len(A):
                if j:
                    j = lps[j - 1]
                else:
                    i += 1

    def lps(self, B):
        len = 0
        i = 1
        lps_table = [0 for _ in range(len(B))]

        while i < len(B):
            if B[len] == B[i]:
                len += 1
                lps_table[i] = len
                i += 1
            elif len:
                len = lps_table[len - 1]
            else:
                i += 1

        return lps_table

    def rotateString(self, A, B):
        N = len(A)
        if N != len(B):
            return False
        if N == 0:
            return True

        return False

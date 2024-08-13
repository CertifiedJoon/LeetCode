class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Premise
        . given m*n matrix, return the distance of nearest 0 for each cell

        Contraint
        . i <= m,n <= 10000
        . i <= m * n <= 10000
        """
        m = len(mat[0])
        n = len(mat)

        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if mat[j][i] != 0:
                    minNeighbor = inf
                    if (j + 1) < n:
                        minNeighbor = min(minNeighbor, mat[j + 1][i])
                    if (i + 1) < m:
                        minNeighbor = min(minNeighbor, mat[j][i + 1])
                    mat[j][i] = minNeighbor + 1

        for j in range(n):
            for i in range(m):
                if mat[j][i] != 0:
                    minNeighbor = inf
                    if (j - 1) >= 0:
                        minNeighbor = min(minNeighbor, mat[j - 1][i])
                    if (i - 1) >= 0:
                        minNeighbor = min(minNeighbor, mat[j][i - 1])
                    mat[j][i] = min(mat[j][i], minNeighbor + 1)

        return mat

class Solution:
    def numSquares(self, n: int) -> int:
        """
        Premise
        . given an integer, return the least number of square numbers that sum to number

        constraint
        . 1 <= n <= 10000
        """
        if n < 4:
            return n

        leastSquareSum = [0 for _ in range(n + 1)]
        leastSquareSum[1] = 1
        leastSquareSum[2] = 2

        for i in range(3, n + 1):
            minLeastSquare = float("inf")
            for root in range(1, int(sqrt(i)) + 1):
                square = root * root
                minLeastSquare = min(minLeastSquare, leastSquareSum[i - square])
            leastSquareSum[i] = 1 + minLeastSquare

        return leastSquareSum[n]

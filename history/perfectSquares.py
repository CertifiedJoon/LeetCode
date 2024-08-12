class Solution:
    def numSquaresDP(self, n: int) -> int:
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

    def numSquaresOptimizedBfs(self, n: int) -> int:
        """
        Premise
        . given an integer, return the least number of square numbers that sum to number

        Constraint
        . 1 <= n <= 10000
        """
        squareNums = [i * i for i in range(1, int(n**0.5) + 1)]
        level = 0
        queue = {n}

        while queue:
            level += 1
            nextQueue = set()

            for remainder in queue:
                for squareNum in squareNums:
                    if remainder == squareNum:
                        return level
                    elif remainder < squareNum:
                        break
                    else:
                        nextQueue.add(remainder - squareNum)

            queue = nextQueue

        return level

    def numSquares2(self, n: int) -> int:
        """
        Premise.
        . given an integer, return the least # of square numbers that sum to n

        Constraint
        . 1 <= n <= 10^4
        """
        if n < 4:
            return n

        leastNumSquares = [0 for _ in range(n + 1)]
        for i in range(4):
            leastNumSquares[i] = i

        for i in range(4, n + 1):
            minNumSquares = float("inf")
            for root in range(1, int(i**0.5) + 1):
                minNumSquares = min(leastNumSquares[i - root**2] + 1, minNumSquares)
            leastNumSquares[i] = minNumSquares

        return leastNumSquares[n]

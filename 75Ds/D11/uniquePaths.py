class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        for y in range(m):
            for x in range(n):
                if x != 0 and y != 0:
                    grid[y][x] = grid[y - 1][x] + grid[y][x - 1]
                elif x == 0 and y != 0:
                    grid[y][x] = grid[y - 1][x]
                elif y == 0 and x != 0:
                    grid[y][x] = grid[y][x - 1]
        print(grid)
        return grid[m - 1][n - 1]
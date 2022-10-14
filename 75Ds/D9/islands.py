class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set() # store visited nodes
        islands = 0
        rl = len(grid)
        cl = len(grid[0])

        for ri in range(rl):
            for ci in range(cl):
                if grid[ri][ci] == "1" and (ri, ci) not in visited:
                    self.dfs(grid, (ri, ci), visited)
                    islands += 1
        
        return islands
    
    def dfs(self, grid, coordinates, visited):
        visited.add(coordinates)
        ri, ci = coordinates
        if (ri - 1, ci) not in visited and 0 <= ri - 1 and grid[ri - 1][ci] == "1":
            self.dfs(grid, (ri - 1, ci), visited)
        if (ri + 1, ci) not in visited and ri + 1 < len(grid) and grid[ri + 1][ci] == "1":
            self.dfs(grid, (ri + 1, ci), visited)
        if (ri, ci - 1) not in visited and ci - 1 >= 0 and grid[ri][ci - 1] == "1":
            self.dfs(grid, (ri, ci - 1), visited)
        if (ri, ci + 1) not in visited and ci + 1 < len(grid[0]) and grid[ri][ci + 1] == "1":
            self.dfs(grid, (ri, ci + 1), visited)
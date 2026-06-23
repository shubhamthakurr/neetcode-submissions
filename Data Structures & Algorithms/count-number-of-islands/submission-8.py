class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def rec(i, j):
            if(i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0):
                return 0

            if(grid[i][j] == "0" or (i,j) in visited):
                return 0
            
            visited.add((i,j))

            rec(i+1, j)
            rec(i, j+1)
            rec(i-1,j)
            rec(i,j-1)

            return 1

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += rec(i,j)

        return res
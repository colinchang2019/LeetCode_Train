class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land, border = 0,0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    land += 1
                    if j+1<m and grid[i][j+1]==1:
                        border += 1
                    if i+1<n and grid[i+1][j]==1:
                        border += 1
        return 4*land- 2*border

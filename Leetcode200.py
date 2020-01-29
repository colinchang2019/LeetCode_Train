from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    res += 1
                    self.bfs(grid,i,j)
        return res
    
    def bfs(self,grid,i,j):
        x = [-1,0,1,0]
        y = [0,1,0,-1]
        dp = deque([(i,j)])
        while dp:
            t = dp.pop()
            grid[t[0]][t[1]] = '0'
            for k in range(4):
                i1,j1 = t[0]+x[k],t[1]+y[k]
                if 0<=i1<len(grid) and 0<=j1<len(grid[0]) and grid[i1][j1]=='1':
                    dp.append((i1,j1))

        

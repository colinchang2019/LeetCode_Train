from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n,m = len(grid),len(grid[0])
        if not grid or not grid[0] or n<3 or m<3:
            return res
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]==0 and self.bfs(grid,i,j,n,m):
                    res += 1
        return res
    
    def bfs(self,grid,i,j,n,m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            return False
        x = [-1,0,1,0]
        y = [0,1,0,-1]
        dp = deque([(i,j)])
        res = True
        while dp:
            t = dp.popleft()
            grid[t[0]][t[1]] = 1
            for k in range(4):
                i1,j1 = t[0]+x[k],t[1]+y[k]
                if 0<=i1<n and 0<=j1<m and grid[i1][j1]==0:
                    dp.append((i1,j1))
                    if i1==0 or i1==n-1 or j1==0 or j1==m-1:
                        res = False
        return res

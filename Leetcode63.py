class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        d = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        d[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    if i>0:
                        d[i][j] += d[i-1][j]
                    if j>0:
                        d[i][j] += d[i][j-1]
        return d[-1][-1]

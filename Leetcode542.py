class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:  # 通常对称的问题，考虑来回两遍动态规划
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==1:
                    matrix[i][j]=r+c
                if i>0:
                    matrix[i][j] = min( matrix[i][j], matrix[i-1][j]+1) 
                if j>0:
                    matrix[i][j] = min(matrix[i][j],matrix[i][j-1]+1)
        for i in range(r)[::-1]:
            for j in range(c)[::-1]:
                if i<r-1:
                    matrix[i][j] = min(matrix[i][j],matrix[i+1][j]+1) 
                if j<c-1:
                    matrix[i][j] = min(matrix[i][j],matrix[i][j+1]+1)
        return matrix

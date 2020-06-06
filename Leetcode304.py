class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix),len(matrix[0]) if matrix else 0
        #self.matrix = matrix
        self.d = matrix.copy()
        for i in range(n):
            for j in range(m):
                a = 0 if i==0 else self.d[i-1][j]
                b = 0 if j==0 else self.d[i][j-1]
                c = self.d[i-1][j-1] if i>0 and j>0 else 0
                self.d[i][j] = matrix[i][j] + a + b - c

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = 0 if row1==0 else self.d[row1-1][col2]
        b = 0 if col1==0 else self.d[row2][col1-1]
        c = self.d[row1-1][col1-1] if row1>0 and col1>0 else 0
        return self.d[row2][col2] - a-b+c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

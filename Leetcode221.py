class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        d = [[0 for _ in range(len(matrix[0]))] for q in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                d[i][j] = int(matrix[i][j])
                res = max(res,matrix[i][j])

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0 or d[i-1][j-1]==0:
                    res = max(res,d[i][j])
                    continue
                m = d[i-1][j-1]
                for n in list(range(m+1))[::-1]:
                    if sum(matrix[i][j-n:j])+sum([matrix[x][j] for x in range(i-n,i)])>=2*n:
                        d[i][j] = n + 1
                        break
                
                res = max(res,d[i][j])
        return res**2

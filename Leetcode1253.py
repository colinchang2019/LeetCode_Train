class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper+lower!=sum(colsum):
            return []
        res = [[0 for i in range(len(colsum))] for _ in range(2)]
        for j in range(len(colsum)):
            res[0][j] = 1 if colsum[j]>0 else 0
            res[1][j] = 1 if colsum[j]==2 else 0
        su1 = sum(res[0])
        for j in range(len(colsum)):
            if su1>upper and res[0][j]==1 and res[1][j]==0:
                res[0][j],res[1][j] = res[1][j],res[0][j]
                su1 -= 1
            if su1==upper:
                break
        if sum(res[0])==upper and sum(res[1])==lower:
            return res
        return []
        

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        l1,l2 = len(A),len(B)
        d = [[0 for j in range(l2+1)] for _ in range(l1+1)]
        res = 0
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if A[i-1]==B[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                    res = max(res,d[i][j])
        return res

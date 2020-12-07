class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        import numpy as np
        a = np.array(A)
        n,m,res = len(A), len(A[0]),0
        for i in range(n):
            if a[i,0]==0:
                a[i,:] = 1 - a[i,:]
        for i in range(m):
            if sum(a[:,i])<((n+1)//2):
                a[:,i] = 1 - a[:,i]
        for x in a:
            res += int("".join([str(i) for i in x]), 2)
        return res

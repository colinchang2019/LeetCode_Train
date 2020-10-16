class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        for i in range(n):
            if A[i]>=0:
                break
        res,j = [],i-1
        while j>-1 or i<n:
            if j==-1:
                res.append(A[i]**2)
                i += 1
                continue
            elif i==n:
                res.append(A[j]**2)
                j -= 1
                continue
            else:
                i1,j1 = A[i]**2,A[j]**2
                if i1<=j1:
                    res.append(i1)
                    i += 1
                else:
                    res.append(j1)
                    j -= 1
        return res

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n<3:
            return False
        for i in range(1,n):
            if A[i]>A[i-1]:
                continue
            elif A[i]==A[i-1]:
                return False
            else:
                if i==1:
                    return False
                break
        for j in range(i, n):
            if A[j]<A[j-1]:
                continue
            else:
                return False
        return True

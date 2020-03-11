class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        ans = sum(A)
        if ans%3!=0: # 首先看和能否被3整除
            return False
        avg = ans//3
        i,j,lsum,rsum = 0,len(A)-1,0,0
        res = False
        while i<j:
            if lsum!=avg or i==0:
                lsum += A[i]
                i += 1
            if rsum!=avg or j==len(A)-1:
                rsum += A[j]
                j -= 1
            if lsum==avg and rsum==avg:
                res = True
                break
        print(i,j)
        return res if i<=j else False

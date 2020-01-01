class Solution:
    def countDigitOne(self, n: int) -> int:
        res,i = 0,10
        while i<=10*n:
            res += n//i*(i//10) + min(i//10,max(0,n%i-i//10+1))
            i = i*10
        return res

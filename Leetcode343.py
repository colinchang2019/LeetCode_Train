class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1
        if n<4: return n-1
        while n>4:
            n -= 3
            res *= 3
        return res*n

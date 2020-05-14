class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1]*(n+1)
        if n<1:
            return dp[-1]
        dp[1] = 10
        for i in range(2,n+1):
            dp[i] = dp[i-1] + (dp[i-1]-dp[i-2])*(10-i+1)
        return dp[-1]

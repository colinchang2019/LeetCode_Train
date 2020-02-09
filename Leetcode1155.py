class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        n = 1000000007
        dp = [[0 for _ in range(target+1)] for i in range(d+1)]
        for i in range(1,d+1):
            for j in range(1,target+1):
                if i==1 and j>f:
                    dp[i][j] = 0
                elif i==1 and j<=f:
                    dp[i][j] = 1
                elif i>1:
                    dp[i][j] = sum([dp[i-1][j-k] for k in range(1,f+1) if j-k>=0])%n
        return dp[d][target]

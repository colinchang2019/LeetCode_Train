class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n<2:
            return 0
        dp1,dp2 = [0]*n, [0]*n # dp1[i]是有股票最大收益；dp2[i]是无股票最大收益
        dp1[0] -= prices[0]
        for i in range(1,n):
            dp1[i] = max(dp1[i-1], dp2[i-1] - prices[i])
            dp2[i] = max(dp2[i-1], dp1[i-1] + prices[i] - fee)
        return dp2[-1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        hold,unhold = [0]*len(prices),[0]*len(prices)
        hold[0],unhold[0] = -prices[0],0
        for i in range(1,len(prices)):
            p = unhold[i-2] if i>=2 else 0
            hold[i] = max(hold[i-1], p-prices[i])
            unhold[i] = max(unhold[i-1], hold[i-1]+prices[i])
        return unhold[-1]

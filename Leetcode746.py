class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n<=2:
            return cost[-1]
        cost.append(0)
        for i in range(2,n+1):
            cost[i] += min(cost[i-1], cost[i-2])
        return cost[-1]

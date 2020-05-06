class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1,7,30]
        dicdays = set(days)

        def dp(i):
            if i>365:
                return 0
            elif i in dicdays:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i+1)
        
        return dp(1)

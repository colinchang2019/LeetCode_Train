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

## 方法2，更快
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]
        durations = [1,7,30]
        day_index = 0 # 标记当天进展到的天
        for i in range(1,days[-1]+1):
            if i != days[day_index]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min([dp[max(i-c,0)]+d for c,d in zip(durations,costs)])
                day_index += 1
        #print(dp)
        return dp[-1]

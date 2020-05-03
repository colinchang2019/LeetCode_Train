class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        if len(nums)<1:
            return 0
        if len(nums)==1:
            return dp[0]
        t = dp[0]
        for i in range(1,len(nums)):
            dp[i] += max(dp[i-1],0)
            t = max(t,dp[i])
        return t

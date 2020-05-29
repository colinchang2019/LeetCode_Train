class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if len(nums)>2:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for n in range(2, len(nums)):
                dp[n] = max(dp[n-1], dp[n-2] + nums[n])
        elif len(nums) == 2:
            dp[1] = max(nums[0], nums[1])
        elif len(nums) == 1:
            dp[0] =  nums[0]
        else:
            return 0
        return dp[len(nums)-1]

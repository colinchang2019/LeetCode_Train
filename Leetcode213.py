class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0: return 0
        if n<=3:
            return max(nums)
        d1 = [0]*n
        d2 = [0]*n
        d1[0],d1[1] = nums[0],max(nums[0], nums[1])
        d2[1],d2[2] = nums[1],max(nums[1],nums[2])
        for i in range(2,n-1):
            d1[i] = max(d1[i-1], d1[i-2] + nums[i])
            d2[i+1] = max(d2[i], d2[i-1] + nums[i+1])
        return max(d1[n-2],d2[n-1])

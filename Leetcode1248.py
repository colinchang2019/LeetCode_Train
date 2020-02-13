class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return 0
        d = [-1]
        for i in range(len(nums)):
            if nums[i]&1==1:
                d.append(i)
        d.append(len(nums))
        res = 0
        for i in range(1,len(d)-k):
            res += (d[i]-d[i-1])*(d[i+k]-d[i+k-1])
        return res

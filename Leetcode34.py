class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0]>target or nums[-1]<target:
            return [-1,-1]
        res = [-1,-1]
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid + 1
        if nums[l]==target:
            res[0] = l
        r = len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid]<=target:
                l = mid + 1
            else:
                r = mid
        if nums[l-1]==target:
            res[1] = l-1
        return res

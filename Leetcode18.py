class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        #print(nums)
        ha = []
        for j in range(len(nums)-3):
            if j>0 and nums[j]==nums[j-1]: continue
            for i in range(j+1,len(nums)-2):
                if i>j+1 and nums[i]==nums[i-1]:
                    continue
                ta = target - nums[i] - nums[j]
                l,r = i+1,len(nums)-1
                while l<r:
                    if nums[l]+nums[r]==ta:
                        ha.append([nums[j],nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l = l+1
                        while l<r and nums[r]==nums[r-1]:
                            r = r-1
                        l = l+1
                        r = r-1
                    elif nums[l]+nums[r]<ta:
                        l = l+1
                    else:
                        r = r-1
        return ha

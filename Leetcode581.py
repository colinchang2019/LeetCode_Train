class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        tmi,tma,left,right = nums[0],nums,-1,-1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                tmi,tma = nums[i],nums[i-1]
                left,right = i-1,i
                break
        if right == -1:
            return 0
        for i in range(right,len(nums)):
            if nums[i]<tma:
                right = i
                tmi = min(tmi,nums[i])
            tma = max(tma,nums[i])
        for i in range(left,-1,-1):
            if nums[i]>tmi:
                left = i
            tmi = min(tmi,nums[i])
        return right-left+1

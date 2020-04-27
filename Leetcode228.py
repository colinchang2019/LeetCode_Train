class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        t = nums[0]
        for i in range(len(nums)):
            if i==0:
                continue
            if nums[i] != nums[i-1]+1:
                if nums[i-1]!=t:
                    res.append(str(t)+"->"+str(nums[i-1]))
                else:
                    res.append(str(t))
                t = nums[i]
        if nums[i]==t:
            res.append(str(t))
        else:
            res.append(str(t)+"->"+str(nums[i]))
        return res

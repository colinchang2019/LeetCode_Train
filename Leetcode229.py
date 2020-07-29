class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res,d,n = [],{},len(nums)//3
        for i in nums:
            x = d.get(i,0)
            if x>n:
                continue
            d[i] = d.get(i,0) + 1
            if d[i]>n:
                res.append(i)
        return res

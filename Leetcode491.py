class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = {(nums[0],)}
        for i in nums[1:]:
            res.update({j+(i,) for j in res if j[-1]<=i})
            res.add((i,))
        return [list(i) for i in res if len(i)>1]
